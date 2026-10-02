use crate::resolve::Workspace;
use crate::run_one::{Outcome, Status};
use anyhow::Result;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::fs;
use std::path::Path;

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct ExerciseProgress {
    #[serde(default)]
    pub status: String,
    #[serde(default)]
    pub attempts: u32,
    #[serde(default, rename = "compileErrors")]
    pub compile_errors: u32,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub first_pass_at: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub last_run_at: Option<String>,
    #[serde(default, rename = "solutionViewed")]
    pub solution_viewed: bool,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct ProgressFile {
    pub version: u32,
    #[serde(rename = "startedAt")]
    pub started_at: String,
    pub exercises: HashMap<String, ExerciseProgress>,
}

impl ProgressFile {
    pub fn load(root: &Path) -> Result<Self> {
        let path = root.join("progress.json");
        if !path.exists() {
            return Ok(Self::new());
        }
        let text = fs::read_to_string(&path).unwrap_or_default();
        match serde_json::from_str(&text) {
            Ok(p) => Ok(p),
            Err(_) => {
                let bak = root.join("progress.json.bak");
                let _ = fs::copy(&path, &bak);
                eprintln!("progress.json was corrupt — backed up and starting fresh.");
                Ok(Self::new())
            }
        }
    }

    pub fn new() -> Self {
        Self {
            version: 1,
            started_at: chrono_now(),
            exercises: HashMap::new(),
        }
    }

    pub fn save(&self, root: &Path) -> Result<()> {
        let path = root.join("progress.json");
        let tmp = root.join("progress.json.tmp");
        let json = serde_json::to_string_pretty(self)?;
        fs::write(&tmp, json)?;
        fs::rename(&tmp, &path)?;
        Ok(())
    }
}

fn chrono_now() -> String {
    time::OffsetDateTime::now_utc()
        .format(&time::format_description::well_known::Rfc3339)
        .unwrap_or_else(|_| "1970-01-01T00:00:00Z".into())
}

pub fn record(root: &Path, outcome: &Outcome) -> Result<()> {
    let mut file = ProgressFile::load(root)?;
    let entry = file
        .exercises
        .entry(outcome.id.clone())
        .or_default();
    entry.last_run_at = Some(chrono_now());

    match outcome.status {
        Status::Pass => {
            if entry.status != "pass" {
                entry.first_pass_at = Some(chrono_now());
            }
            entry.status = "pass".into();
        }
        Status::CompileError => {
            entry.compile_errors += 1;
        }
        Status::Fail | Status::Runtime | Status::Timeout | Status::MissingExpected => {
            entry.attempts += 1;
        }
    }

    file.save(root)
}

pub fn is_level_complete(ws: &Workspace, level_dir: &str) -> Result<bool> {
    let file = ProgressFile::load(&ws.root)?;
    for name in ws.list_exercises_in_level(level_dir)? {
        let id = format!("{level_dir}/{name}");
        match file.exercises.get(&id) {
            Some(e) if e.status == "pass" => {}
            _ => return Ok(false),
        }
    }
    Ok(true)
}

pub fn level_summary(ws: &Workspace, level_dir: &str) -> Result<(usize, usize)> {
    let file = ProgressFile::load(&ws.root)?;
    let names = ws.list_exercises_in_level(level_dir)?;
    let done = names
        .iter()
        .filter(|n| {
            file.exercises
                .get(&format!("{level_dir}/{n}"))
                .is_some_and(|e| e.status == "pass")
        })
        .count();
    Ok((done, names.len()))
}

pub fn first_unfinished_before(ws: &Workspace, id: &str) -> Result<Option<String>> {
    let ex = ws.exercise_from_id(id)?;
    for level in ws.list_levels()? {
        let num = Workspace::level_num(&level);
        if num >= ex.level_num {
            break;
        }
        if !is_level_complete(ws, &level)? {
            for name in ws.list_exercises_in_level(&level)? {
                let eid = format!("{level}/{name}");
                let file = ProgressFile::load(&ws.root)?;
                if file.exercises.get(&eid).is_none_or(|e| e.status != "pass") {
                    return Ok(Some(eid));
                }
            }
        }
    }
    Ok(None)
}

pub fn get_exercise(root: &Path, id: &str) -> Result<ExerciseProgress> {
    let file = ProgressFile::load(root)?;
    Ok(file.exercises.get(id).cloned().unwrap_or_default())
}

pub fn set_solution_viewed(root: &Path, id: &str) -> Result<()> {
    let mut file = ProgressFile::load(root)?;
    file.exercises.entry(id.to_string()).or_default().solution_viewed = true;
    file.save(root)
}

pub fn clear_exercise(root: &Path, id: &str) -> Result<()> {
    let mut file = ProgressFile::load(root)?;
    file.exercises.remove(id);
    file.save(root)
}

pub fn clear_level(root: &Path, ws: &Workspace, level_dir: &str) -> Result<()> {
    let mut file = ProgressFile::load(root)?;
    for name in ws.list_exercises_in_level(level_dir)? {
        file.exercises.remove(&format!("{level_dir}/{name}"));
    }
    file.save(root)
}

pub fn longest_stuck(root: &Path) -> Option<(String, u32)> {
    let file = ProgressFile::load(root).ok()?;
    file.exercises
        .iter()
        .filter(|(_, e)| e.status != "pass")
        .max_by_key(|(_, e)| e.attempts)
        .map(|(id, e)| (id.clone(), e.attempts))
}
