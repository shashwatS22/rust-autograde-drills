use crate::resolve::Workspace;
use crate::run_one::run;
use crate::Config;
use anyhow::{Context, Result};
use std::fs;
use walkdir::WalkDir;

pub fn gen_expected(ws: &Workspace, level_filter: Option<u32>) -> Result<()> {
    for level in ws.list_levels()? {
        if let Some(n) = level_filter {
            if Workspace::level_num(&level) != n {
                continue;
            }
        }
        for name in ws.list_exercises_in_level(&level)? {
            let id = format!("{level}/{name}");
            let ex = ws.exercise_from_id(&id)?;
            if ws.checks_path(&ex).exists() {
                continue;
            }
            let outcome = run(ws, &Config::default(), &id, true)?;
            if outcome.status != crate::run_one::Status::Pass {
                anyhow::bail!(
                    "gen-expected: solution for {id} did not pass: {:?}",
                    outcome.status
                );
            }
            let expected_path = ws.expected_path(&ex);
            if let Some(parent) = expected_path.parent() {
                fs::create_dir_all(parent)?;
            }
            if outcome.actual.trim().is_empty() {
                anyhow::bail!("gen-expected: {id} produced empty output");
            }
            fs::write(&expected_path, &outcome.actual)?;
            println!("wrote {}", expected_path.display());
        }
    }
    Ok(())
}

pub fn verify_all(ws: &Workspace, level_filter: Option<u32>) -> Result<(usize, usize)> {
    let cfg = Config::default();
    let mut pass = 0usize;
    let mut total = 0usize;
    for level in ws.list_levels()? {
        if let Some(n) = level_filter {
            if Workspace::level_num(&level) != n {
                continue;
            }
        }
        for name in ws.list_exercises_in_level(&level)? {
            total += 1;
            let id = format!("{level}/{name}");
            let outcome = run(ws, &cfg, &id, true)?;
            if outcome.status == crate::run_one::Status::Pass {
                pass += 1;
            } else {
                eprintln!("FAIL verify: {id} {:?}", outcome.status);
            }
        }
    }
    Ok((pass, total))
}

pub fn verify_readmes(ws: &Workspace) -> Result<()> {
    let tmp = ws.root.join("target/readme-check");
    fs::create_dir_all(&tmp)?;
    let mut count = 0usize;
    for level in ws.list_levels()? {
        let readme = ws.level_crate_dir(&level).join("README.md");
        if !readme.exists() {
            continue;
        }
        let text = fs::read_to_string(&readme)?;
        let blocks = extract_rust_blocks(&text);
        for (i, block) in blocks.iter().enumerate() {
            let src = wrap_snippet(block);
            let path = tmp.join(format!("{}_{i}.rs", level.replace('-', "_")));
            fs::write(&path, src)?;
            let status = std::process::Command::new("rustc")
                .arg("--edition")
                .arg("2024")
                .arg(&path)
                .arg("-o")
                .arg(tmp.join(format!("{}_{i}", level.replace('-', "_"))))
                .status()
                .context("rustc")?;
            if !status.success() {
                anyhow::bail!("README snippet failed to compile in {level} block {i}");
            }
            count += 1;
        }
    }
    println!("Compiled {count} README snippets.");
    Ok(())
}

fn extract_rust_blocks(md: &str) -> Vec<String> {
    let mut blocks = Vec::new();
    let mut in_block = false;
    let mut current = String::new();
    for line in md.lines() {
        if line.trim_start().starts_with("```rust") {
            in_block = true;
            current.clear();
            continue;
        }
        if in_block && line.trim_start().starts_with("```") {
            in_block = false;
            blocks.push(current.clone());
            continue;
        }
        if in_block {
            current.push_str(line);
            current.push('\n');
        }
    }
    blocks
}

fn wrap_snippet(block: &str) -> String {
    let trimmed = block.trim();
    if trimmed.contains("fn main") {
        trimmed.to_string()
    } else {
        format!("fn main() {{\n{trimmed}\n}}")
    }
}

pub fn read_stub_template(path: &std::path::Path) -> Result<String> {
    fs::read_to_string(path).with_context(|| format!("read stub {}", path.display()))
}

pub fn restore_stub_from_git(ws: &Workspace, id: &str) -> Result<()> {
    let ex = ws.exercise_from_id(id)?;
    let _ = ex;
    Ok(())
}

pub fn walk_readme_snippets(root: &std::path::Path) -> Result<Vec<std::path::PathBuf>> {
    let mut paths = Vec::new();
    for entry in WalkDir::new(root.join("levels")).into_iter().filter_map(|e| e.ok()) {
        if entry.file_name() == "README.md" {
            paths.push(entry.path().to_path_buf());
        }
    }
    Ok(paths)
}
