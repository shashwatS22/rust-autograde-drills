use anyhow::{Context, Result};
use std::path::{Path, PathBuf};

#[derive(Clone)]
pub struct Workspace {
    pub root: PathBuf,
}

#[derive(Debug, Clone)]
pub struct ExerciseRef {
    pub id: String,
    pub level_dir: String,
    pub name: String,
    pub level_num: u32,
    pub package: String,
    pub sol_package: String,
}

impl Workspace {
    pub fn new(root: PathBuf) -> Self {
        Self { root }
    }

    pub fn levels_dir(&self) -> PathBuf {
        self.root.join("levels")
    }

    pub fn list_levels(&self) -> Result<Vec<String>> {
        let mut levels = Vec::new();
        for entry in std::fs::read_dir(self.levels_dir())? {
            let entry = entry?;
            if entry.file_type()?.is_dir() {
                let name = entry.file_name().to_string_lossy().into_owned();
                if name.chars().next().is_some_and(|c| c.is_ascii_digit()) {
                    levels.push(name);
                }
            }
        }
        levels.sort();
        Ok(levels)
    }

    pub fn level_num(level_dir: &str) -> u32 {
        level_dir
            .split('-')
            .next()
            .and_then(|s| s.parse().ok())
            .unwrap_or(0)
    }

    pub fn package_name(level_dir: &str) -> String {
        format!("level-{level_dir}")
    }

    pub fn sol_package_name(level_dir: &str) -> String {
        format!("sol-{level_dir}")
    }

    pub fn parse_id(id: &str) -> Result<(String, String)> {
        let (level, name) = id
            .split_once('/')
            .with_context(|| format!("invalid exercise id {id:?}, want level/name"))?;
        Ok((level.to_string(), name.to_string()))
    }

    pub fn exercise_from_id(&self, id: &str) -> Result<ExerciseRef> {
        let (level_dir, name) = Self::parse_id(id)?;
        Ok(ExerciseRef {
            id: id.to_string(),
            level_num: Self::level_num(&level_dir),
            package: Self::package_name(&level_dir),
            sol_package: Self::sol_package_name(&level_dir),
            level_dir,
            name,
        })
    }

    pub fn stub_path(&self, ex: &ExerciseRef) -> PathBuf {
        self.levels_dir()
            .join(&ex.level_dir)
            .join("src/bin")
            .join(format!("{}.rs", ex.name))
    }

    pub fn expected_path(&self, ex: &ExerciseRef) -> PathBuf {
        self.levels_dir()
            .join(&ex.level_dir)
            .join("expected")
            .join(format!("{}.txt", ex.name))
    }

    pub fn checks_path(&self, ex: &ExerciseRef) -> PathBuf {
        self.levels_dir()
            .join(&ex.level_dir)
            .join("checks")
            .join(format!("{}.rs", ex.name))
    }

    pub fn solution_bin_path(&self, ex: &ExerciseRef) -> PathBuf {
        self.root
            .join("solutions")
            .join(&ex.level_dir)
            .join("src/bin")
            .join(format!("{}.rs", ex.name))
    }

    pub fn level_crate_dir(&self, level_dir: &str) -> PathBuf {
        self.levels_dir().join(level_dir)
    }

    pub fn list_exercises_in_level(&self, level_dir: &str) -> Result<Vec<String>> {
        let bin_dir = self.level_dir(level_dir).join("src/bin");
        if !bin_dir.exists() {
            return Ok(Vec::new());
        }
        let mut names = Vec::new();
        for entry in std::fs::read_dir(&bin_dir)? {
            let entry = entry?;
            let path = entry.path();
            if path.extension().is_some_and(|e| e == "rs") {
                names.push(
                    path.file_stem()
                        .unwrap()
                        .to_string_lossy()
                        .into_owned(),
                );
            }
        }
        names.sort();
        Ok(names)
    }

    fn level_dir(&self, level_dir: &str) -> PathBuf {
        self.levels_dir().join(level_dir)
    }

    pub fn id_from_path(&self, path: &Path) -> Option<String> {
        let path = path.canonicalize().ok()?;
        let levels = self.levels_dir().canonicalize().ok()?;
        let rel = path.strip_prefix(&levels).ok()?;
        let parts: Vec<_> = rel.components().collect();
        if parts.len() < 3 {
            return None;
        }
        let level = parts[0].as_os_str().to_string_lossy();
        if parts[1].as_os_str() != "src" || parts[2].as_os_str() != "bin" {
            return None;
        }
        if parts.len() == 4 {
            let file = parts[3].as_os_str().to_string_lossy();
            if file.ends_with(".rs") && !file.ends_with(".test.rs") {
                let name = file.trim_end_matches(".rs");
                return Some(format!("{level}/{name}"));
            }
        }
        None
    }

    pub fn is_level_non_bin_source(&self, path: &Path) -> Option<String> {
        let path = path.canonicalize().ok()?;
        let levels = self.levels_dir().canonicalize().ok()?;
        let rel = path.strip_prefix(&levels).ok()?;
        let s = rel.to_string_lossy();
        if s.contains("/src/bin/") {
            return None;
        }
        if s.contains("/src/") {
            let level = rel.components().next()?.as_os_str().to_string_lossy().into_owned();
            return Some(level);
        }
        None
    }

    pub fn all_exercise_ids(&self) -> Result<Vec<String>> {
        let mut ids = Vec::new();
        for level in self.list_levels()? {
            for name in self.list_exercises_in_level(&level)? {
                ids.push(format!("{level}/{name}"));
            }
        }
        Ok(ids)
    }

    pub fn hints_path(&self, level_dir: &str) -> PathBuf {
        self.level_dir(level_dir).join("hints.toml")
    }

    pub fn load_hint(&self, ex: &ExerciseRef) -> Option<String> {
        let path = self.hints_path(&ex.level_dir);
        let text = std::fs::read_to_string(path).ok()?;
        let table: toml::Table = toml::from_str(&text).ok()?;
        table
            .get(&ex.name)
            .and_then(|v| v.as_str())
            .map(|s| s.to_string())
    }

    pub fn exercises_target_dir(&self) -> PathBuf {
        self.root.join("target/exercises")
    }

    pub fn has_lib_crate(&self, level_dir: &str) -> bool {
        self.level_crate_dir(level_dir).join("src/lib.rs").exists()
    }

    pub fn first_exercise_in_level(&self, level_dir: &str) -> Option<String> {
        self.list_exercises_in_level(level_dir)
            .ok()
            .and_then(|v| v.into_iter().next())
    }

    pub fn default_regrade_id(&self, level_dir: &str) -> Option<String> {
        self.first_exercise_in_level(level_dir)
            .map(|name| format!("{level_dir}/{name}"))
    }
}
