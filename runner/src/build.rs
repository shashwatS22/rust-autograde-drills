use anyhow::{Context, Result};
use serde_json::Value;
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
    let output = Command::new("cargo")
        .arg("clippy")
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
        .stderr(Stdio::piped())
        .output()
        .context("spawn cargo clippy")?;

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
