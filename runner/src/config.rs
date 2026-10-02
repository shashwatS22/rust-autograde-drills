use anyhow::{Context, Result};
use serde::Deserialize;
use std::path::{Path, PathBuf};

#[derive(Debug, Clone, Deserialize)]
#[serde(default)]
pub struct Config {
    #[serde(default = "default_clear_screen")]
    pub clear_screen: bool,
    #[serde(default = "default_timeout")]
    pub timeout_ms: u64,
    #[serde(default = "default_true")]
    pub strict_progression: bool,
    #[serde(default = "default_unlock")]
    pub solution_unlock_after_failures: u32,
    #[serde(default = "default_true")]
    pub show_warnings_on_pass: bool,
    #[serde(default)]
    pub clippy_hints: bool,
    #[serde(default = "default_max_errors")]
    pub max_errors_shown: usize,
}

fn default_clear_screen() -> bool {
    true
}
fn default_timeout() -> u64 {
    5000
}
fn default_true() -> bool {
    true
}
fn default_unlock() -> u32 {
    3
}
fn default_max_errors() -> usize {
    3
}

impl Default for Config {
    fn default() -> Self {
        Self {
            clear_screen: true,
            timeout_ms: 5000,
            strict_progression: true,
            solution_unlock_after_failures: 3,
            show_warnings_on_pass: true,
            clippy_hints: false,
            max_errors_shown: 3,
        }
    }
}

impl Config {
    pub fn load(root: &Path) -> Result<Self> {
        let path = root.join("config.toml");
        if !path.exists() {
            return Ok(Self::default());
        }
        let text = std::fs::read_to_string(&path).with_context(|| format!("read {}", path.display()))?;
        toml::from_str(&text).context("parse config.toml")
    }
}

pub fn find_workspace_root() -> Result<PathBuf> {
    let mut dir = std::env::current_dir()?;
    loop {
        if dir.join("Cargo.toml").exists() && dir.join("levels").is_dir() {
            return Ok(dir);
        }
        if !dir.pop() {
            anyhow::bail!("could not find workspace root (need Cargo.toml and levels/)");
        }
    }
}
