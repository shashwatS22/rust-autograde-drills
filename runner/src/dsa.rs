use crate::progress::{is_level_complete, level_summary, ProgressFile};
use crate::resolve::Workspace;
use anyhow::{Context, Result};
use serde::Deserialize;
use std::fs;
#[derive(Debug, Deserialize)]
struct DsaSection {
    id: String,
    name: String,
    unlock_after_level: String,
    problem_count: u32,
    checklist: String,
}

#[derive(Debug, Deserialize)]
struct DsaConfig {
    sections: Vec<DsaSection>,
}

pub fn print_dsa_status(ws: &Workspace) -> Result<()> {
    let cfg_path = ws.root.join("dsa").join("sections.toml");
    let text = fs::read_to_string(&cfg_path)
        .with_context(|| format!("read {}", cfg_path.display()))?;
    let cfg: DsaConfig = toml::from_str(&text).context("parse dsa/sections.toml")?;
    let progress = ProgressFile::load(&ws.root)?;

    println!("Striver A2Z — unlocked sections (from repo progress)\n");
    for section in &cfg.sections {
        let unlocked = is_level_complete(ws, &section.unlock_after_level)?;
        let (done, total) = level_summary(ws, &section.unlock_after_level)?;
        let marker = if unlocked { "✓" } else { " " };
        println!(
            "{marker} {name} — {count} problems (unlocks after `{unlock}`, level {done}/{total})",
            name = section.name,
            count = section.problem_count,
            unlock = section.unlock_after_level,
            done = done,
            total = total,
        );
        if unlocked {
            println!("    checklist: {}", section.checklist);
        }
    }
    let passed = progress
        .exercises
        .values()
        .filter(|e| e.status == "pass")
        .count();
    println!("\nRepo exercises passed overall: {passed}");
    Ok(())
}
