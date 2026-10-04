use crate::config::Config;
use crate::progress::level_summary;
use crate::resolve::Workspace;
use crate::run_one::{Mode, Outcome, Status};
use owo_colors::OwoColorize;

pub fn banner(cfg: &Config) {
    if cfg.clear_screen {
        print!("\x1B[2J\x1B[H");
    }
    println!("{}", "rust-bootcamp".bold().cyan());
    println!();
}

pub fn progression_blocked(id: &str, blocker: &str) {
    println!(
        "{} Finish {} before working on {}.",
        "⏸".yellow(),
        blocker.bold(),
        id.dimmed()
    );
    println!();
}

pub fn result(cfg: &Config, ws: &Workspace, outcome: &Outcome) {
    if cfg.clear_screen {
        print!("\x1B[2J\x1B[H");
    }

    if outcome.checks_tampered {
        println!(
            "{} The checks for {} have been edited.",
            "⚠".yellow(),
            outcome.id.bold()
        );
        println!();
        println!("  Those are the thing being graded — changing them doesn't change whether");
        println!("  your code is right. Run `cargo reset-checks {}` to put them back.", outcome.id);
        println!();
        return;
    }

    let ms = outcome.build_ms + outcome.run_ms;
    match outcome.status {
        Status::Pass => {
            println!(
                "{} {} {} ({}ms)",
                "✓".green(),
                "PASS".green().bold(),
                outcome.id.bold(),
                ms
            );
            if let Ok((done, total)) = level_summary(ws, &outcome.level) {
                let num = Workspace::level_num(&outcome.level);
                println!(
                    "        Level {:02} — {}/{} done",
                    num, done, total
                );
                if done == total && total > 0 {
                    celebrate_level(ws, &outcome.level);
                }
            }
            if cfg.show_warnings_on_pass {
                show_warnings(&outcome.warnings, &outcome.clippy);
            }
        }
        Status::CompileError => {
            println!(
                "{} {} {}",
                "✗".red(),
                "DOESN'T COMPILE".red().bold(),
                outcome.id.bold()
            );
            println!();
            for d in &outcome.diagnostics {
                print!("{d}");
            }
            if outcome.diagnostics_extra > 0 {
                println!(
                    "… and {} more errors — fix the first one and most of these will go away.",
                    outcome.diagnostics_extra
                );
            }
            if let Some(code) = outcome.error_codes.first() {
                println!();
                println!(
                    "  This is normal. Read the arrows in the message above.  `rustc --explain {}` has a longer write-up.",
                    code
                );
            }
        }
        Status::Fail => match outcome.mode {
            Mode::Checks => print_checks_fail(outcome),
            Mode::Output => print_output_fail(outcome),
        },
        Status::Runtime => {
            println!(
                "{} {} {}",
                "✗".red(),
                "ERROR".red().bold(),
                outcome.id.bold()
            );
            println!();
            print_runtime_stderr(&outcome.stderr);
        }
        Status::Timeout => {
            println!(
                "{} {} {}",
                "✗".red(),
                "TIMEOUT".red().bold(),
                outcome.id.bold()
            );
            println!();
            println!("  Timed out — you may have an infinite loop.");
        }
        Status::MissingExpected => {
            println!(
                "{} {} {} — missing expected output file",
                "✗".red(),
                "ERROR".red().bold(),
                outcome.id.bold()
            );
        }
    }
    println!();
}

fn print_output_fail(outcome: &Outcome) {
    println!(
        "{} {} {}",
        "✗".red(),
        "FAIL".red().bold(),
        outcome.id.bold()
    );
    println!();
    println!("  {:>4}  {:16}  {}", "line", "expected", "your output");
    println!("  {:>4}  {:16}  {}", "────", "────────────────", "────────────────");
    let diff = outcome.diff();
    for line in &diff.lines {
        let mark = if line.is_first_diff {
            "      ← first difference".red().to_string()
        } else {
            String::new()
        };
        println!(
            "  {:>4}  {:16}  {} {}",
            line.line_no,
            truncate(&line.expected, 16),
            truncate(&line.actual, 16),
            mark
        );
    }
    if diff.truncated > 0 {
        println!("  … {} more lines", diff.truncated);
    }
    if let Some(h) = &outcome.hint {
        println!();
        println!("  Hint: {}", h.italic());
    }
}

fn print_checks_fail(outcome: &Outcome) {
    println!(
        "{} {} {}",
        "✗".red(),
        "FAIL".red().bold(),
        outcome.id.bold()
    );
    println!();
    for c in &outcome.checks {
        if c.passed {
            println!("  {} {}", "✓".green(), c.name);
        } else {
            println!("  {} {}", "✗".red(), c.name);
        }
    }
    let passed = outcome.checks.iter().filter(|c| c.passed).count();
    println!();
    println!(
        "  {} checks, {} passed, {} failed.",
        outcome.checks.len(),
        passed,
        outcome.checks.len() - passed
    );
}

fn print_runtime_stderr(stderr: &str) {
    let lines: Vec<_> = stderr.lines().collect();
    for line in lines.iter().take(8) {
        println!("  {line}");
    }
    if lines.len() > 8 {
        println!("  …");
    }
}

fn show_warnings(warnings: &[String], clippy: &[String]) {
    let mut shown = 0;
    if !warnings.is_empty() || !clippy.is_empty() {
        println!();
        println!("  Two things the compiler would like you to know:");
    }
    for w in warnings.iter().chain(clippy.iter()) {
        if shown >= 2 {
            break;
        }
        for line in w.lines().take(3) {
            println!("  {line}");
        }
        shown += 1;
    }
}

fn truncate(s: &str, max: usize) -> String {
    if s.chars().count() <= max {
        s.to_string()
    } else {
        format!("{}…", s.chars().take(max - 1).collect::<String>())
    }
}

fn celebrate_level(ws: &Workspace, level_dir: &str) {
    let num = Workspace::level_num(level_dir);
    println!();
    println!("{}", "═".repeat(50).green());
    println!(
        "{}  Level {:02} complete!",
        "★".green(),
        num
    );
    if let Ok(levels) = ws.list_levels() {
        if let Some(pos) = levels.iter().position(|l| l == level_dir) {
            if let Some(next) = levels.get(pos + 1) {
                println!("  Next up: {}", next.bold());
            }
        }
    }
    println!("{}", "═".repeat(50).green());
}

pub fn print_progress_dashboard(ws: &Workspace) -> anyhow::Result<()> {
    use crate::phases::PhasesFile;
    use crate::progress::{longest_stuck, ProgressFile};
    let file = ProgressFile::load(&ws.root)?;
    let mut total = 0usize;
    let mut done = 0usize;
    println!("{}", "Progress".bold());
    println!();
    let phases = PhasesFile::load(&ws.root).ok();
    if let Some(ref phases) = phases {
        for phase in &phases.phase {
            let mut phase_total = 0usize;
            let mut phase_done = 0usize;
            for level in ws.list_levels()? {
                let num = Workspace::level_num(&level);
                if num < phase.level_start || num > phase.level_end {
                    continue;
                }
                let names = ws.list_exercises_in_level(&level)?;
                let level_done = names
                    .iter()
                    .filter(|n| {
                        file.exercises
                            .get(&format!("{level}/{n}"))
                            .is_some_and(|e| e.status == "pass")
                    })
                    .count();
                phase_total += names.len();
                phase_done += level_done;
            }
            let pct = if phase_total == 0 {
                0
            } else {
                (phase_done * 100) / phase_total
            };
            println!(
                "  {} {} {}/{}",
                phase.name.bold(),
                progress_bar(pct),
                phase_done,
                phase_total
            );
        }
        println!();
    }
    for level in ws.list_levels()? {
        let names = ws.list_exercises_in_level(&level)?;
        let level_done = names
            .iter()
            .filter(|n| {
                file.exercises
                    .get(&format!("{level}/{n}"))
                    .is_some_and(|e| e.status == "pass")
            })
            .count();
        total += names.len();
        done += level_done;
        let pct = if names.is_empty() {
            0
        } else {
            (level_done * 100) / names.len()
        };
        let bar = progress_bar(pct);
        println!(
            "  {} {} {} {}/{}",
            level,
            bar,
            format!("{pct}%").dimmed(),
            level_done,
            names.len()
        );
    }
    println!();
    println!("  Total: {done}/{total}");
    let compile_errors: u32 = file.exercises.values().map(|e| e.compile_errors).sum();
    println!("  Compile errors survived: {compile_errors}");
    if let Some((id, attempts)) = longest_stuck(&ws.root) {
        if attempts > 0 {
            println!("  Longest stuck: {} ({} failed runs)", id, attempts);
        }
    }
    Ok(())
}

fn progress_bar(pct: usize) -> String {
    let filled = pct / 10;
    format!("[{}{}]", "#".repeat(filled), "-".repeat(10 - filled))
}
