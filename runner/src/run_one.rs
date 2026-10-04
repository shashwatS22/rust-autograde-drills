use crate::build::{cargo_build_bin, cargo_clippy_bin, filter_errors};
use crate::config::Config;
use crate::grade::{compare, Diff};
use crate::resolve::{ExerciseRef, Workspace};
use anyhow::{Context, Result};
use sha2::{Digest, Sha256};
use std::fs;
use std::io::Read;
use std::path::Path;
use std::process::{Command, Stdio};
use std::thread;
use std::time::{Duration, Instant};

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Status {
    Pass,
    Fail,
    CompileError,
    Runtime,
    Timeout,
    MissingExpected,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Mode {
    Output,
    Checks,
}

#[derive(Debug, Clone)]
pub struct CheckResult {
    pub name: String,
    pub passed: bool,
    pub detail: String,
}

#[derive(Debug, Clone)]
pub struct Outcome {
    pub id: String,
    pub level: String,
    pub name: String,
    pub status: Status,
    pub mode: Mode,
    pub expected: String,
    pub actual: String,
    pub stderr: String,
    pub diagnostics: Vec<String>,
    pub diagnostics_extra: usize,
    pub error_codes: Vec<String>,
    pub warnings: Vec<String>,
    pub clippy: Vec<String>,
    pub checks: Vec<CheckResult>,
    pub build_ms: u128,
    pub run_ms: u128,
    pub hint: Option<String>,
    pub checks_tampered: bool,
}

impl Outcome {
    pub fn diff(&self) -> Diff {
        crate::grade::build_diff(&self.expected, &self.actual, 20)
    }
}

pub fn run(ws: &Workspace, cfg: &Config, id: &str, use_solution: bool) -> Result<Outcome> {
    let ex = ws.exercise_from_id(id)?;
    let cfg = cfg.for_level(&ws.root, &ex.level_dir);
    let hint = ws.load_hint(&ex);
    let checks_path = ws.checks_path(&ex);
    let is_checks = checks_path.exists();
    let mode = if is_checks { Mode::Checks } else { Mode::Output };

    if is_checks && !use_solution && checks_tampered(ws, &ex)? {
        return Ok(Outcome {
            id: id.to_string(),
            level: ex.level_dir.clone(),
            name: ex.name.clone(),
            status: Status::Fail,
            mode,
            expected: String::new(),
            actual: String::new(),
            stderr: String::new(),
            diagnostics: vec![],
            diagnostics_extra: 0,
            error_codes: vec![],
            warnings: vec![],
            clippy: vec![],
            checks: vec![],
            build_ms: 0,
            run_ms: 0,
            hint,
            checks_tampered: true,
        });
    }

    let package = if use_solution {
        ex.sol_package.clone()
    } else {
        ex.package.clone()
    };

    let target_dir = ws.exercises_target_dir();
    let build = cargo_build_bin(
        &ws.root,
        &target_dir,
        &package,
        &ex.name,
        is_checks,
    )?;

    if !build.errors.is_empty() {
        let (diag, extra) = filter_errors(build.errors, cfg.max_errors_shown);
        let codes = extract_error_codes(&diag);
        return Ok(Outcome {
            id: id.to_string(),
            level: ex.level_dir.clone(),
            name: ex.name.clone(),
            status: Status::CompileError,
            mode,
            expected: String::new(),
            actual: String::new(),
            stderr: String::new(),
            diagnostics: diag,
            diagnostics_extra: extra,
            error_codes: codes,
            warnings: build.warnings,
            clippy: vec![],
            checks: vec![],
            build_ms: build.build_ms,
            run_ms: 0,
            hint,
            checks_tampered: false,
        });
    }

    let exe = build
        .executable
        .context("cargo build succeeded but no executable")?;

    let level_dir = ws.level_crate_dir(&ex.level_dir);
    let run_start = Instant::now();

    if is_checks {
        let (checks, passed, detail) = run_test_binary(&exe, &level_dir, cfg.timeout_ms)?;
        let status = if passed {
            Status::Pass
        } else {
            Status::Fail
        };
        let mut outcome = Outcome {
            id: id.to_string(),
            level: ex.level_dir.clone(),
            name: ex.name.clone(),
            status,
            mode,
            expected: String::new(),
            actual: detail,
            stderr: String::new(),
            diagnostics: vec![],
            diagnostics_extra: 0,
            error_codes: vec![],
            warnings: build.warnings,
            clippy: vec![],
            checks,
            build_ms: build.build_ms,
            run_ms: run_start.elapsed().as_millis(),
            hint,
            checks_tampered: false,
        };
        if outcome.status == Status::Pass && cfg.clippy_hints {
            outcome.clippy = cargo_clippy_bin(&ws.root, &target_dir, &package, &ex.name)?
                .into_iter()
                .take(2)
                .collect();
        }
        return Ok(outcome);
    }

    let (stdout, stderr, run_status) = run_executable(&exe, &level_dir, cfg.timeout_ms)?;

    match run_status {
        RunStatus::Timeout => {
            return Ok(base_outcome(
                &ex,
                id,
                mode,
                Status::Timeout,
                String::new(),
                stdout,
                stderr,
                build.build_ms,
                run_start.elapsed().as_millis(),
                hint,
                build.warnings,
            ));
        }
        RunStatus::RuntimeError => {
            return Ok(base_outcome(
                &ex,
                id,
                mode,
                Status::Runtime,
                String::new(),
                stdout,
                stderr,
                build.build_ms,
                run_start.elapsed().as_millis(),
                hint,
                build.warnings,
            ));
        }
        RunStatus::Ok => {}
    }

    let expected_path = ws.expected_path(&ex);
    if !expected_path.exists() {
        return Ok(base_outcome(
            &ex,
            id,
            mode,
            Status::MissingExpected,
            String::new(),
            stdout,
            stderr,
            build.build_ms,
            run_start.elapsed().as_millis(),
            hint,
            build.warnings,
        ));
    }

    let expected = fs::read_to_string(&expected_path).context("read expected")?;
    let status = if compare(&expected, &stdout) {
        Status::Pass
    } else {
        Status::Fail
    };

    let mut outcome = base_outcome(
        &ex,
        id,
        mode,
        status,
        expected,
        stdout,
        stderr,
        build.build_ms,
        run_start.elapsed().as_millis(),
        hint,
        build.warnings,
    );

    if outcome.status == Status::Pass && cfg.clippy_hints {
        outcome.clippy = cargo_clippy_bin(&ws.root, &target_dir, &package, &ex.name)?
            .into_iter()
            .take(2)
            .collect();
    }

    Ok(outcome)
}

fn base_outcome(
    ex: &ExerciseRef,
    id: &str,
    mode: Mode,
    status: Status,
    expected: String,
    actual: String,
    stderr: String,
    build_ms: u128,
    run_ms: u128,
    hint: Option<String>,
    warnings: Vec<String>,
) -> Outcome {
    Outcome {
        id: id.to_string(),
        level: ex.level_dir.clone(),
        name: ex.name.clone(),
        status,
        mode,
        expected,
        actual,
        stderr,
        diagnostics: vec![],
        diagnostics_extra: 0,
        error_codes: vec![],
        warnings,
        clippy: vec![],
        checks: vec![],
        build_ms,
        run_ms,
        hint,
        checks_tampered: false,
    }
}

enum RunStatus {
    Ok,
    Timeout,
    RuntimeError,
}

fn run_executable(
    exe: &Path,
    cwd: &Path,
    timeout_ms: u64,
) -> Result<(String, String, RunStatus)> {
    let mut child = Command::new(exe)
        .current_dir(cwd)
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn()
        .context("spawn exercise")?;

    let mut stdout_handle = child.stdout.take();
    let mut stderr_handle = child.stderr.take();

    let deadline = Duration::from_millis(timeout_ms);
    let start = Instant::now();
    loop {
        if let Some(status) = child.try_wait()? {
            let mut stdout = String::new();
            let mut stderr = String::new();
            if let Some(mut out) = stdout_handle.take() {
                let _ = out.read_to_string(&mut stdout);
            }
            if let Some(mut err) = stderr_handle.take() {
                let _ = err.read_to_string(&mut stderr);
            }
            if !status.success() || !stderr.trim().is_empty() {
                return Ok((stdout, stderr, RunStatus::RuntimeError));
            }
            return Ok((stdout, stderr, RunStatus::Ok));
        }
        if start.elapsed() >= deadline {
            let _ = child.kill();
            let _ = child.wait();
            return Ok((String::new(), String::new(), RunStatus::Timeout));
        }
        thread::sleep(Duration::from_millis(10));
    }
}

fn run_test_binary(
    exe: &Path,
    cwd: &Path,
    timeout_ms: u64,
) -> Result<(Vec<CheckResult>, bool, String)> {
    let exe = exe.to_path_buf();
    let cwd = cwd.to_path_buf();
    let handle = thread::spawn(move || {
        Command::new(&exe)
            .arg("--test-threads=1")
            .current_dir(&cwd)
            .output()
    });

    let deadline = Duration::from_millis(timeout_ms);
    let start = Instant::now();
    loop {
        if handle.is_finished() {
            let output = handle.join().unwrap()?;
            let stdout = String::from_utf8_lossy(&output.stdout);
            let stderr = String::from_utf8_lossy(&output.stderr);
            let combined = format!("{stdout}\n{stderr}");
            let checks = parse_libtest(&combined);
            let passed = output.status.success() && checks.iter().all(|c| c.passed);
            return Ok((checks, passed, combined));
        }
        if start.elapsed() >= deadline {
            return Ok((vec![], false, "Timed out running tests.".into()));
        }
        thread::sleep(Duration::from_millis(10));
    }
}

fn parse_libtest(output: &str) -> Vec<CheckResult> {
    let mut checks = Vec::new();
    for line in output.lines() {
        let line = line.trim();
        if let Some(rest) = line.strip_prefix("test ") {
            if let Some((name, status)) = rest.split_once(" ... ") {
                let passed = status == "ok";
                checks.push(CheckResult {
                    name: name.to_string(),
                    passed,
                    detail: String::new(),
                });
            }
        }
    }
    checks
}

fn extract_error_codes(diagnostics: &[String]) -> Vec<String> {
    let mut codes = Vec::new();
    for d in diagnostics {
        if let Some(idx) = d.find("error[E") {
            let rest = &d[idx + 6..];
            if let Some(end) = rest.find(']') {
                codes.push(format!("E{}", &rest[..end]));
            }
        }
    }
    codes
}

fn checks_tampered(ws: &Workspace, ex: &ExerciseRef) -> Result<bool> {
    let lock_path = ws.root.join("checks.lock");
    if !lock_path.exists() {
        return Ok(false);
    }
    let text = fs::read_to_string(&lock_path)?;
    let table: toml::Table = toml::from_str(&text).unwrap_or_default();
    let checks_path = ws.checks_path(ex);
    let key = format!("{}/{}", ex.level_dir, ex.name);
    let Some(expected_hash) = table.get(&key).and_then(|v| v.as_str()) else {
        return Ok(false);
    };
    let actual = hash_file(&checks_path)?;
    Ok(actual != expected_hash)
}

pub fn hash_file(path: &Path) -> Result<String> {
    let bytes = fs::read(path)?;
    let mut hasher = Sha256::new();
    hasher.update(bytes);
    Ok(format!("{:x}", hasher.finalize()))
}

pub fn rebuild_checks_lock(ws: &Workspace) -> Result<()> {
    let mut table = toml::Table::new();
    for level in ws.list_levels()? {
        let checks_dir = ws.level_crate_dir(&level).join("checks");
        if !checks_dir.exists() {
            continue;
        }
        for entry in fs::read_dir(checks_dir)? {
            let entry = entry?;
            let path = entry.path();
            if path.extension().is_some_and(|e| e == "rs") {
                let name = path.file_stem().unwrap().to_string_lossy();
                let key = format!("{level}/{name}");
                table.insert(key, toml::Value::String(hash_file(&path)?));
            }
        }
    }
    let out = toml::to_string_pretty(&table)?;
    fs::write(ws.root.join("checks.lock"), out)?;
    Ok(())
}

pub fn backup_checks(ws: &Workspace) -> Result<()> {
    let backup = ws.root.join(".checks-backup");
    fs::create_dir_all(&backup)?;
    for level in ws.list_levels()? {
        let checks_dir = ws.level_crate_dir(&level).join("checks");
        if !checks_dir.exists() {
            continue;
        }
        let dest_level = backup.join(&level);
        fs::create_dir_all(&dest_level)?;
        for entry in fs::read_dir(checks_dir)? {
            let entry = entry?;
            fs::copy(entry.path(), dest_level.join(entry.file_name()))?;
        }
    }
    Ok(())
}

pub fn restore_checks(ws: &Workspace, level: &str, name: &str) -> Result<()> {
    let src = ws
        .root
        .join(".checks-backup")
        .join(level)
        .join(format!("{name}.rs"));
    let dest = ws.checks_path(&ws.exercise_from_id(&format!("{level}/{name}"))?);
    fs::copy(src, dest)?;
    Ok(())
}
