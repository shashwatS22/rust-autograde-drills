use anyhow::{Context, Result};
use serde::Deserialize;
use std::path::Path;

#[derive(Debug, Clone, Deserialize)]
pub struct PhaseDef {
    pub name: String,
    pub level_start: u32,
    pub level_end: u32,
}

#[derive(Debug, Clone, Deserialize)]
pub struct PhasesFile {
    pub phase: Vec<PhaseDef>,
}

impl PhasesFile {
    pub fn load(root: &Path) -> Result<Self> {
        let path = root.join("phases.toml");
        let text = std::fs::read_to_string(&path).with_context(|| format!("read {}", path.display()))?;
        toml::from_str(&text).context("parse phases.toml")
    }

    pub fn phase_for_level(&self, level_num: u32) -> Option<&PhaseDef> {
        self.phase
            .iter()
            .find(|p| level_num >= p.level_start && level_num <= p.level_end)
    }
}
