use anyhow::{Context, Result};
use serde_json::Value;
use std::fs;
use std::path::{Path, PathBuf};
use std::process::{Command, Stdio};
use std::time::Instant;

#[derive(Debug, Clone)]
pub struct BuildOutcome {
    pub errors: Vec<String>,
    pub warnings: Vec<String>,
    pub executable: Option<PathBuf>,
    pub build_ms: u128,
}

pub fn cargo_build_bin(
    root: &Path,
    target_dir: &Path,
    package: &str,
    bin: &str,
    for_test: bool,
) -> Result<BuildOutcome> {
    let start = Instant::now();
    if let Some(outcome) = rustc_standalone(root, target_dir, package, bin, for_test, start)? {
        return Ok(outcome);
    }

    let mut cmd = if for_test {
        let mut c = Command::new("cargo");
        c.arg("test")
            .arg("--manifest-path")
            .arg(root.join("Cargo.toml"))
            .arg("-p")
            .arg(package)
            .arg("--bin")
            .arg(bin)
            .arg("--no-run");
        c
    } else {
        let mut c = Command::new("cargo");
        c.arg("build")
            .arg("--manifest-path")
            .arg(root.join("Cargo.toml"))
            .arg("-p")
            .arg(package)
            .arg("--bin")
            .arg(bin);
        c
    };

    cmd.arg("--message-format=json-diagnostic-rendered-ansi")
        .env("CARGO_TARGET_DIR", target_dir)
        .env("CARGO_TERM_COLOR", "always")
        .stdout(Stdio::piped())
        .stderr(Stdio::piped());
    apply_job_cap(&mut cmd);

    let output = cmd.output().context("spawn cargo")?;
    let stdout = String::from_utf8_lossy(&output.stdout);
    let mut errors = Vec::new();
    let mut warnings = Vec::new();
    let mut executable = None;
    let mut error_codes_seen = Vec::new();

    for line in stdout.lines() {
        let line = line.trim();
        if line.is_empty() {
            continue;
        }
        let Ok(v) = serde_json::from_str::<Value>(line) else {
            continue;
        };
        let reason = v.get("reason").and_then(|r| r.as_str()).unwrap_or("");
        match reason {
            "compiler-message" => {
                let msg = v.get("message").context("message")?;
                let level = msg.get("level").and_then(|l| l.as_str()).unwrap_or("");
                let rendered = msg
                    .get("rendered")
                    .and_then(|r| r.as_str())
                    .unwrap_or("")
                    .to_string();
                if level == "failure-note" {
                    continue;
                }
                if level == "error" {
                    if rendered.contains("For more information about this error, try") {
                        if let Some(code) = msg.get("code").and_then(|c| c.get("code")).and_then(|c| c.as_str()) {
                            error_codes_seen.push(code.to_string());
                        }
                        continue;
                    }
                    if rendered.contains("this error originates in the macro") {
                        continue;
                    }
                    errors.push(rendered);
                } else if level == "warning" {
                    warnings.push(rendered);
                }
            }
            "compiler-artifact" => {
                let target = v.get("target").and_then(|t| t.get("name")).and_then(|n| n.as_str());
                if target != Some(bin) {
                    continue;
                }
                if for_test {
                    let profile = v.get("profile").and_then(|p| p.get("test")).and_then(|t| t.as_bool());
                    if profile != Some(true) {
                        continue;
                    }
                }
                if let Some(exe) = v.get("executable").and_then(|e| e.as_str()) {
                    executable = Some(PathBuf::from(exe));
                }
            }
            _ => {}
        }
    }

    if !errors.is_empty() && !error_codes_seen.is_empty() {
        // Footer handled in report
    }

    Ok(BuildOutcome {
        errors,
        warnings,
        executable,
        build_ms: start.elapsed().as_millis(),
    })
}

pub fn filter_errors(errors: Vec<String>, max: usize) -> (Vec<String>, usize) {
    let extra = errors.len().saturating_sub(max);
    (errors.into_iter().take(max).collect(), extra)
}

pub fn cargo_clippy_bin(
    root: &Path,
    target_dir: &Path,
    package: &str,
    bin: &str,
) -> Result<Vec<String>> {
    let mut cmd = Command::new("cargo");
    cmd.arg("clippy")
        .arg("--manifest-path")
        .arg(root.join("Cargo.toml"))
        .arg("-p")
        .arg(package)
        .arg("--bin")
        .arg(bin)
        .arg("--message-format=json-diagnostic-rendered-ansi")
        .arg("-q")
        .env("CARGO_TARGET_DIR", target_dir)
        .env("CARGO_TERM_COLOR", "always")
        .stdout(Stdio::piped())
        .stderr(Stdio::piped());
    apply_job_cap(&mut cmd);
    let output = cmd.output().context("spawn cargo clippy")?;

    let stdout = String::from_utf8_lossy(&output.stdout);
    let mut warnings = Vec::new();
    for line in stdout.lines() {
        let Ok(v) = serde_json::from_str::<Value>(line) else {
            continue;
        };
        if v.get("reason").and_then(|r| r.as_str()) != Some("compiler-message") {
            continue;
        }
        let msg = v.get("message").unwrap();
        let level = msg.get("level").and_then(|l| l.as_str()).unwrap_or("");
        if level == "warning" {
            if let Some(r) = msg.get("rendered").and_then(|x| x.as_str()) {
                warnings.push(r.to_string());
            }
        }
    }
    Ok(warnings)
}

/// Zero-dependency exercise files are one `rustc` invocation. Cargo would
/// otherwise reload every workspace member (levels, solutions, and projects)
/// on each save.
fn rustc_standalone(
    root: &Path,
    target_dir: &Path,
    package: &str,
    bin: &str,
    for_test: bool,
    start: Instant,
) -> Result<Option<BuildOutcome>> {
    let Some((src, edition)) = standalone_bin(root, package, bin)? else {
        return Ok(None);
    };

    let out_dir = target_dir.join("fast");
    fs::create_dir_all(&out_dir)?;
    let exe_name = if cfg!(windows) {
        format!("{bin}.exe")
    } else {
        bin.to_string()
    };
    let exe = out_dir.join(exe_name);

    let mut cmd = Command::new("rustc");
    cmd.arg("--edition")
        .arg(&edition)
        .arg("--error-format=json")
        .arg("--json")
        .arg("diagnostic-rendered-ansi")
        .arg("-C")
        .arg("debuginfo=0")
        .arg("-C")
        .arg("opt-level=0")
        .arg("--crate-name")
        .arg("exercise")
        .arg("-o")
        .arg(&exe)
        .arg(&src);
    if for_test {
        cmd.arg("--test");
    }
    let output = cmd
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .output()
        .context("spawn rustc")?;

    let stderr = String::from_utf8_lossy(&output.stderr);
    let mut errors = Vec::new();
    let mut warnings = Vec::new();
    for line in stderr.lines() {
        let Ok(v) = serde_json::from_str::<Value>(line) else {
            continue;
        };
        if v.get("$message_type").and_then(|t| t.as_str()) != Some("diagnostic") {
            continue;
        }
        absorb_diagnostic(&v, &mut errors, &mut warnings);
    }

    let compiled = output.status.success() && errors.is_empty();
    if !compiled {
        let _ = fs::remove_file(&exe);
        if errors.is_empty() {
            let fallback = String::from_utf8_lossy(&output.stderr);
            if !fallback.trim().is_empty() {
                errors.push(fallback.into_owned());
            }
        }
    }

    Ok(Some(BuildOutcome {
        errors,
        warnings,
        executable: compiled.then_some(exe),
        build_ms: start.elapsed().as_millis(),
    }))
}

fn standalone_bin(root: &Path, package: &str, bin: &str) -> Result<Option<(PathBuf, String)>> {
    let Some(dir) = locate_package(root, package) else {
        return Ok(None);
    };
    let manifest_path = dir.join("Cargo.toml");
    let text = fs::read_to_string(&manifest_path)
        .with_context(|| format!("read {}", manifest_path.display()))?;
    let manifest: toml::Value = toml::from_str(&text)
        .with_context(|| format!("parse {}", manifest_path.display()))?;
    if !is_standalone(&manifest) {
        return Ok(None);
    }
    let src = dir.join("src/bin").join(format!("{bin}.rs"));
    if !src.is_file() {
        return Ok(None);
    }
    Ok(Some((src, package_edition(&manifest))))
}

fn locate_package(root: &Path, package: &str) -> Option<PathBuf> {
    let mut candidates = Vec::new();
    if let Some(rest) = package.strip_prefix("level-") {
        candidates.push(root.join("levels").join(rest));
    }
    if let Some(rest) = package.strip_prefix("sol-") {
        candidates.push(root.join("solutions").join(rest));
    }
    candidates.push(root.join("projects").join(package));
    candidates.push(root.join(package));
    candidates.into_iter().find(|p| p.join("Cargo.toml").is_file())
}

fn is_standalone(manifest: &toml::Value) -> bool {
    if manifest.get("lib").is_some() || manifest.get("target").is_some() {
        return false;
    }
    dep_table_empty(manifest, "dependencies")
        && dep_table_empty(manifest, "build-dependencies")
        && dep_table_empty(manifest, "dev-dependencies")
}

fn dep_table_empty(manifest: &toml::Value, key: &str) -> bool {
    match manifest.get(key) {
        None => true,
        Some(toml::Value::Table(table)) => table.is_empty(),
        Some(_) => false,
    }
}

fn package_edition(manifest: &toml::Value) -> String {
    manifest
        .get("package")
        .and_then(|pkg| pkg.get("edition"))
        .and_then(|edition| edition.as_str())
        .unwrap_or("2024")
        .to_string()
}

fn absorb_diagnostic(msg: &Value, errors: &mut Vec<String>, warnings: &mut Vec<String>) {
    let level = msg.get("level").and_then(|l| l.as_str()).unwrap_or("");
    let rendered = msg
        .get("rendered")
        .and_then(|r| r.as_str())
        .unwrap_or("")
        .to_string();
    let message = msg.get("message").and_then(|m| m.as_str()).unwrap_or("");
    if level == "failure-note" || level == "note" || level == "help" {
        return;
    }
    if message.starts_with("aborting due to")
        || message.ends_with("warning emitted")
        || message.ends_with("warnings emitted")
    {
        return;
    }
    if rendered.contains("For more information about this error, try")
        || rendered.contains("this error originates in the macro")
    {
        return;
    }
    if level == "error" && !rendered.is_empty() {
        errors.push(rendered);
    } else if level == "warning" && !rendered.is_empty() {
        warnings.push(rendered);
    }
}

fn apply_job_cap(cmd: &mut Command) {
    if std::env::var_os("CARGO_BUILD_JOBS").is_none() {
        cmd.env("CARGO_BUILD_JOBS", build_jobs().to_string());
    }
}

fn build_jobs() -> usize {
    let cpus = std::thread::available_parallelism()
        .map(|n| n.get())
        .unwrap_or(2);
    let cap = match physical_memory_gb().unwrap_or(8) {
        0..=8 => 1,
        9..=16 => 2,
        17..=24 => 3,
        _ => 4,
    };
    cap.min(cpus).max(1)
}

fn physical_memory_gb() -> Option<u64> {
    #[cfg(target_os = "macos")]
    {
        let out = Command::new("sysctl")
            .args(["-n", "hw.memsize"])
            .output()
            .ok()?;
        let bytes: u64 = String::from_utf8(out.stdout).ok()?.trim().parse().ok()?;
        return Some(bytes / (1024 * 1024 * 1024));
    }
    #[cfg(target_os = "linux")]
    {
        let text = fs::read_to_string("/proc/meminfo").ok()?;
        for line in text.lines() {
            if let Some(rest) = line.strip_prefix("MemTotal:") {
                let kb: u64 = rest.split_whitespace().next()?.parse().ok()?;
                return Some(kb / (1024 * 1024));
            }
        }
        return None;
    }
    #[cfg(not(any(target_os = "macos", target_os = "linux")))]
    {
        None
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn root() -> PathBuf {
        Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("..")
            .canonicalize()
            .unwrap()
    }

    #[test]
    fn zero_dep_bins_skip_cargo() {
        let root = root();
        assert!(standalone_bin(&root, "level-01-print-and-variables", "01-hello")
            .unwrap()
            .is_some());
        assert!(standalone_bin(&root, "level-29-async-tokio", "01-async-fn")
            .unwrap()
            .is_none());
        assert!(standalone_bin(&root, "level-16-modules-errors-io", "01-inline-module")
            .unwrap()
            .is_none());
        assert!(standalone_bin(&root, "level-41-ffi", "01-ffi-add")
            .unwrap()
            .is_none());
    }

    #[test]
    fn fast_path_compiles_output_and_test_bins() {
        let root = root();
        let target = root.join("target/exercises");
        let output = cargo_build_bin(
            &root,
            &target,
            "level-01-print-and-variables",
            "01-hello",
            false,
        )
        .unwrap();
        assert!(output.errors.is_empty(), "{:?}", output.errors);
        let exe = output.executable.expect("executable");
        let ran = Command::new(&exe).output().unwrap();
        assert!(ran.status.success());
        assert_eq!(String::from_utf8_lossy(&ran.stdout), "Hello, World!\n");

        let tested = cargo_build_bin(&root, &target, "level-08-functions", "01-add", true).unwrap();
        assert!(tested.errors.is_empty(), "{:?}", tested.errors);
        assert!(tested.executable.is_some());
    }
}
