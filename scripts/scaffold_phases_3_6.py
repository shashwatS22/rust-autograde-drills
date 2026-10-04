#!/usr/bin/env python3
"""Scaffold levels 17–48 (Phases 3–6). Run from repo root. Does not modify levels 01–16."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

import hashlib

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent

LEVEL_DEPS: dict[str, list[str]] = {
    "25-error-design": ["thiserror", "anyhow"],
    "29-async-tokio": ["tokio"],
    "30-serde": ["serde", "serde_json"],
    "31-axum-routing": ["axum", "tokio", "tower", "http-body-util", "hyper"],
    "32-axum-extractors": ["axum", "tokio", "tower", "serde", "serde_json", "http-body-util", "hyper"],
    "33-axum-errors": ["axum", "tokio", "tower", "serde", "serde_json", "http-body-util", "hyper"],
    "34-tower-and-tracing": [
        "axum",
        "tokio",
        "tower",
        "tower-http",
        "tracing",
        "tracing-subscriber",
        "http-body-util",
        "hyper",
    ],
    "35-sqlx": ["sqlx", "tokio"],
    "36-auth-and-config": [
        "axum",
        "tokio",
        "tower",
        "serde",
        "serde_json",
        "jsonwebtoken",
        "argon2",
        "dotenvy",
        "http-body-util",
        "hyper",
    ],
    "37-rayon-and-pools": ["rayon"],
    "41-ffi": ["cc"],
    "43-cli-clap": ["clap"],
    "44-wasm-bindgen": ["wasm-bindgen"],
    "45-web-sys-dom": ["wasm-bindgen", "web-sys", "js-sys"],
    "46-leptos-components": ["leptos"],
    "47-leptos-signals": ["leptos"],
    "48-leptos-server-fns": ["leptos", "serde", "serde_json"],
}


def _import_content():
    if str(SCRIPTS) not in sys.path:
        sys.path.insert(0, str(SCRIPTS))
    from phases_3_6_common import Exercise
    from phases_3_6_content import LEVELS_WITH_EXERCISES

    return Exercise, LEVELS_WITH_EXERCISES


def level_cargo_toml(level_dir: str) -> str:
    pkg = f"level-{level_dir}"
    deps = LEVEL_DEPS.get(level_dir, [])
    dep_lines = "\n".join(f"{d} = {{ workspace = true }}" for d in deps)
    extra = ""
    if level_dir == "41-ffi":
        extra = "\n[build-dependencies]\ncc = { workspace = true }\n"
    return f"""[package]
name = "{pkg}"
edition.workspace = true
version.workspace = true
publish.workspace = true
{extra}
[dependencies]
{dep_lines}
"""


def sol_cargo_toml(level_dir: str) -> str:
    return level_cargo_toml(level_dir).replace(f"level-{level_dir}", f"sol-{level_dir}", 1)


def level_toml(level_dir: str, phase: int) -> str:
    lines = [f"phase = {phase}"]
    if LEVEL_DEPS.get(level_dir):
        lines.append("timeout_ms = 20000")
    return "\n".join(lines) + "\n"


def write_stub(ex: Exercise, level_dir: str, path: Path) -> None:
    lines = [
        f"//! {level_dir} / {ex.name}",
        "//!",
        "//! TASK",
        f"//! {ex.task}",
        "//!",
    ]
    if ex.test_graded:
        lines.extend(
            [
                "//! SIGNATURE",
                f"//! {ex.signature}",
                "//!",
                "//! This exercise is graded by the checks at the bottom of the file, not by",
                "//! printed output. Leave `main` empty.",
                "//!",
            ]
        )
    elif ex.expected_hint:
        lines.extend(["//! EXPECTED OUTPUT", f"//! {ex.expected_hint}", ""])
    else:
        lines.append("")
    if ex.test_graded:
        body = [ex.stub_body, "", "fn main() {}", "", "// ---- CHECKS: DO NOT EDIT ----", "#[cfg(test)]", f'#[path = "../../checks/{ex.name}.rs"]', "mod tests;"]
    else:
        body = ["fn main() {"]
        if ex.given:
            body.extend(["    // ---- GIVEN ----", *[f"    {g}" for g in ex.given.split("\n")], "    // ---------------", ""])
        body.extend(["    // Your code below", "    todo!()", "}"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines + body) + "\n", encoding="utf-8")


def solution_body(ex: Exercise, level_dir: str) -> str:
    code = ex.solution.rstrip()
    if ex.test_graded and "fn main()" not in code:
        code += "\n\nfn main() {}\n"
    if ex.test_graded:
        code += f"""

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/{level_dir}/checks/{ex.name}.rs"]
mod tests;
"""
    return code


def scaffold_ffi_native(level_root: Path) -> None:
    native = level_root / "native"
    native.mkdir(parents=True, exist_ok=True)
    (native / "add.c").write_text(
        '#include <stdint.h>\n\nint32_t add_int(int32_t a, int32_t b) {\n    return a + b;\n}\n',
        encoding="utf-8",
    )
    (level_root / "build.rs").write_text(
        'fn main() {\n    cc::Build::new().file("native/add.c").compile("native_add");\n}\n',
        encoding="utf-8",
    )


def backup_checks_all() -> None:
    backup = ROOT / ".checks-backup"
    backup.mkdir(parents=True, exist_ok=True)
    for checks in (ROOT / "levels").glob("*/checks"):
        lv = checks.parent.name
        dest = backup / lv
        dest.mkdir(parents=True, exist_ok=True)
        for f in checks.glob("*.rs"):
            shutil.copy2(f, dest / f.name)


def write_expected_from_solutions(levels_with_exercises) -> None:
    target = ROOT / "target" / "exercises"
    env = os.environ.copy()
    env["CARGO_TARGET_DIR"] = str(target)
    manifest = str(ROOT / "Cargo.toml")
    for level_dir, _, _, exercises in levels_with_exercises:
        sol_pkg = f"sol-{level_dir}"
        for ex in exercises:
            if ex.test_graded:
                continue
            nm = ex.name
            subprocess.run(
                ["cargo", "build", "--manifest-path", manifest, "-p", sol_pkg, "--bin", nm],
                cwd=ROOT,
                env=env,
                check=True,
            )
            exe = target / "debug" / nm
            proc = subprocess.run(
                [str(exe)],
                cwd=ROOT / "levels" / level_dir,
                capture_output=True,
                text=True,
                check=True,
            )
            out_path = ROOT / "levels" / level_dir / "expected" / f"{nm}.txt"
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(proc.stdout, encoding="utf-8")


def rebuild_checks_lock() -> None:
    table: dict[str, str] = {}
    for checks in sorted((ROOT / "levels").glob("*/checks")):
        lv = checks.parent.name
        for f in sorted(checks.glob("*.rs")):
            h = hashlib.sha256(f.read_bytes()).hexdigest()
            table[f"{lv}/{f.stem}"] = h
    lines = [f'{k} = "{v}"' for k, v in sorted(table.items())]
    (ROOT / "checks.lock").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_readme(level_dir: str, title: str, phase: int) -> None:
    path = ROOT / "levels" / level_dir / "README.md"
    path.write_text(
        f"# Level {level_dir} — {title}\n\n"
        f"Phase {phase} drills. Work through the numbered exercises in order.\n\n"
        "## Exercises\n"
        "Save each file under `src/bin/` to grade it with `cargo dev`.\n",
        encoding="utf-8",
    )


def write_build_spec_md(levels_with_exercises) -> None:
    out = ROOT / "reference" / "CURSOR-BUILD-SPEC-PHASES-3-6.md"
    parts = [
        "# Phases 3–6 exercise bank (levels 17–48)\n",
        "Concise index of scaffolded drills. See each level README for learner-facing text.\n",
    ]
    for level_dir, phase, title, exercises in levels_with_exercises:
        parts.append(f"\n## Level {level_dir} — {title} (phase {phase})\n\n")
        parts.append("| File | Grading | Task |\n|---|---|---|\n")
        for ex in exercises:
            mode = "[T]" if ex.test_graded else "output"
            task = ex.task.replace("|", "\\|")
            parts.append(f"| `{ex.name}` | {mode} | {task} |\n")
    out.write_text("".join(parts), encoding="utf-8")


def main() -> int:
    os.chdir(ROOT)
    _, levels_with_exercises = _import_content()

    for level_dir, phase, title, exercises in levels_with_exercises:
        lv_root = ROOT / "levels" / level_dir
        sol_root = ROOT / "solutions" / level_dir
        lv_root.mkdir(parents=True, exist_ok=True)
        sol_root.mkdir(parents=True, exist_ok=True)
        (lv_root / "Cargo.toml").write_text(level_cargo_toml(level_dir), encoding="utf-8")
        (sol_root / "Cargo.toml").write_text(sol_cargo_toml(level_dir), encoding="utf-8")
        (lv_root / "level.toml").write_text(level_toml(level_dir, phase), encoding="utf-8")
        write_readme(level_dir, title, phase)
        if level_dir == "41-ffi":
            scaffold_ffi_native(lv_root)
            scaffold_ffi_native(sol_root)
        checks_dir = lv_root / "checks"
        for ex in exercises:
            stub_path = lv_root / "src" / "bin" / f"{ex.name}.rs"
            sol_path = sol_root / "src" / "bin" / f"{ex.name}.rs"
            write_stub(ex, level_dir, stub_path)
            sol_path.parent.mkdir(parents=True, exist_ok=True)
            sol_path.write_text(solution_body(ex, level_dir), encoding="utf-8")
            backup = ROOT / ".stub-backups" / f"{level_dir}__{ex.name}.rs"
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(stub_path, backup)
            if ex.test_graded and ex.check:
                checks_dir.mkdir(parents=True, exist_ok=True)
                (checks_dir / f"{ex.name}.rs").write_text(ex.check.rstrip() + "\n", encoding="utf-8")

    write_build_spec_md(levels_with_exercises)
    backup_checks_all()
    rebuild_checks_lock()
    write_expected_from_solutions(levels_with_exercises)

    subprocess.run(
        ["cargo", "run", "--release", "-p", "runner", "--bin", "cli", "--", "gen-expected"],
        cwd=ROOT,
        check=True,
    )
    proc = subprocess.run(
        ["cargo", "run", "--release", "-p", "runner", "--bin", "cli", "--", "verify"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    print(proc.stdout)
    if proc.stderr:
        print(proc.stderr, file=sys.stderr)
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
