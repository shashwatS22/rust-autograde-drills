use anyhow::{Context, Result};
use runner::config::{find_workspace_root, Config};
use runner::maint::{gen_expected, verify_all, verify_readmes};
use runner::progress::{clear_exercise, clear_level, get_exercise, set_solution_viewed};
use runner::report::print_progress_dashboard as dashboard;
use runner::resolve::Workspace;
use runner::run_one::{restore_checks, run};
use std::env;
use std::fs;
use std::io::{self, Write};

fn main() -> Result<()> {
    let root = find_workspace_root()?;
    let cfg = Config::load(&root)?;
    let ws = Workspace::new(root.clone());
    let mut args = env::args().skip(1);
    let cmd = args.next().unwrap_or_else(|| "help".into());

    match cmd.as_str() {
        "grade" => {
            let id = args.next().context("usage: grade <level/name>")?;
            let outcome = run(&ws, &cfg, &id, false)?;
            runner::progress::record(&root, &outcome)?;
            runner::report::result(&cfg, &ws, &outcome);
        }
        "grade-level" => {
            let nn = args.next().context("usage: grade-level <NN>")?;
            let level = find_level_by_num(&ws, &nn)?;
            for name in ws.list_exercises_in_level(&level)? {
                let id = format!("{level}/{name}");
                let outcome = run(&ws, &cfg, &id, false)?;
                runner::progress::record(&root, &outcome)?;
                println!("{:?} {}", outcome.status, id);
            }
        }
        "progress" => {
            dashboard(&ws)?;
        }
        "solution" => {
            let mut force = false;
            let mut id = String::new();
            for a in args {
                if a == "--force" {
                    force = true;
                } else {
                    id = a;
                }
            }
            if id.is_empty() {
                anyhow::bail!("usage: solution <id> [--force]");
            }
            let prog = get_exercise(&root, &id)?;
            if !force && prog.attempts < cfg.solution_unlock_after_failures {
                let need = cfg.solution_unlock_after_failures - prog.attempts;
                println!("Solution locked. {need} more failed attempt(s) needed (compile errors don't count).");
                return Ok(());
            }
            let ex = ws.exercise_from_id(&id)?;
            let path = ws.solution_bin_path(&ex);
            let text = fs::read_to_string(&path).with_context(|| format!("read {}", path.display()))?;
            print!("{text}");
            set_solution_viewed(&root, &id)?;
        }
        "reset" => {
            let target = args.next().context("usage: reset <id|level NN>")?;
            print!("Type yes to confirm reset: ");
            io::stdout().flush()?;
            let mut line = String::new();
            io::stdin().read_line(&mut line)?;
            if line.trim() != "yes" {
                println!("Cancelled.");
                return Ok(());
            }
            if target.starts_with("level ") || target.len() <= 2 {
                let nn = target.trim_start_matches("level ").trim();
                let level = find_level_by_num(&ws, nn)?;
                clear_level(&root, &ws, &level)?;
                restore_level_stubs(&ws, &level)?;
                println!("Reset level {level}");
            } else {
                clear_exercise(&root, &target)?;
                restore_stub(&ws, &target)?;
                println!("Reset {target}");
            }
        }
        "reset-checks" => {
            let id = args.next().context("usage: reset-checks <id>")?;
            let (level, name) = Workspace::parse_id(&id)?;
            restore_checks(&ws, &level, &name)?;
            runner::run_one::rebuild_checks_lock(&ws)?;
            println!("Restored checks for {id}");
        }
        "gen-expected" => {
            let level = args.next().map(|s| s.parse().ok()).flatten();
            gen_expected(&ws, level)?;
        }
        "verify" => {
            let mut level_filter = None;
            let rest: Vec<_> = args.collect();
            let mut i = 0;
            while i < rest.len() {
                if rest[i] == "--level" && i + 1 < rest.len() {
                    level_filter = rest[i + 1].parse().ok();
                    i += 2;
                } else {
                    level_filter = rest[i].parse().ok();
                    i += 1;
                }
            }
            let (pass, total) = verify_all(&ws, level_filter)?;
            println!("{pass}/{total}");
            if pass != total {
                std::process::exit(1);
            }
        }
        "verify-readmes" => verify_readmes(&ws)?,
        "warm" => {
            let nn = args.next().context("usage: warm <NN>")?;
            let level = find_level_by_num(&ws, &nn)?;
            let pkg = Workspace::package_name(&level);
            let names = ws.list_exercises_in_level(&level)?;
            let mut cmd = std::process::Command::new("cargo");
            cmd.arg("build")
                .arg("--manifest-path")
                .arg(root.join("Cargo.toml"))
                .arg("-p")
                .arg(&pkg);
            for name in &names {
                cmd.arg("--bin").arg(name);
            }
            cmd.env(
                "CARGO_TARGET_DIR",
                ws.exercises_target_dir(),
            );
            let status = cmd.status().context("cargo warm build")?;
            if !status.success() {
                std::process::exit(1);
            }
            println!("Warmed level {level} ({pkg}), {} bins.", names.len());
        }
        "help" | _ => print_help(),
    }
    Ok(())
}

fn print_help() {
    println!(
        "Commands: grade, grade-level, progress, solution, reset, reset-checks, gen-expected, verify, verify-readmes, warm"
    );
}

fn find_level_by_num(ws: &Workspace, nn: &str) -> Result<String> {
    let n: u32 = nn.parse().context("level number")?;
    for level in ws.list_levels()? {
        if Workspace::level_num(&level) == n {
            return Ok(level);
        }
    }
    anyhow::bail!("no level {n}");
}

fn restore_stub(ws: &Workspace, id: &str) -> Result<()> {
    let ex = ws.exercise_from_id(id)?;
    let backup = ws.root.join(".stub-backups").join(format!("{}.rs", id.replace('/', "__")));
    let stub = ws.stub_path(&ex);
    if backup.exists() {
        fs::copy(&backup, &stub)?;
    }
    Ok(())
}

fn restore_level_stubs(ws: &Workspace, level: &str) -> Result<()> {
    for name in ws.list_exercises_in_level(level)? {
        restore_stub(ws, &format!("{level}/{name}"))?;
    }
    Ok(())
}
