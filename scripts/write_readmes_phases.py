#!/usr/bin/env python3
"""Generate README.md for levels 17-48 (and fill any missing 01-16)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVELS = ROOT / "levels"

EXTRA = {
    "17-traits": (
        "Traits",
        ["defining and implementing traits", "default methods", "`Display` vs `Debug`"],
        "Define a trait and implement it on a struct. Most exercises are test-graded.",
        ["Implementing a trait for the wrong type — match the impl block to the type."],
    ),
    "25-error-design": (
        "Error design",
        ["`thiserror` for libraries", "`anyhow` for applications", "custom error types"],
        "Run `cargo warm 25` before starting — this level pulls in crates.",
        ["Using `unwrap()` everywhere instead of returning `Result`."],
    ),
    "29-async-tokio": (
        "Async & Tokio",
        ["`async fn` and `.await`", "Tokio runtime", "deterministic tests with `pause()`"],
        "Run `cargo warm 29` first. Checks use `tokio::time::pause()` — no real sleeping.",
        ["Blocking the executor with `std::thread::sleep` inside async code."],
    ),
    "31-axum-routing": (
        "Axum routing",
        ["`Router` and routes", "in-process testing with `oneshot`", "no binding ports"],
        "Handlers are graded with `tower::ServiceExt::oneshot` — never start a server in a drill.",
        ["Forgetting `.with_state()` when handlers need shared state."],
    ),
    "35-sqlx": (
        "SQLx",
        ["SQLite in memory", "runtime queries", "migrations in drills"],
        "Drills use `sqlite::memory:` only. Postgres is for `projects/api`.",
        ["Using `query!` without offline data — prefer runtime API in drills."],
    ),
    "40-unsafe": (
        "Unsafe Rust",
        ["raw pointers", "invariants", "sound abstractions"],
        "Every `unsafe` block must uphold an invariant stated in your comment.",
        ["Calling `unsafe` to silence the borrow checker without documenting why it's sound."],
    ),
    "41-ffi": (
        "FFI",
        ["`extern \"C\"`", "calling C from Rust", "requires a system C compiler"],
        "Level bundles `native/add.c`. Install Xcode CLT or `gcc` before this level.",
        ["Mismatching C and Rust types at the FFI boundary."],
    ),
    "46-leptos-components": (
        "Leptos components",
        ["SSR with `view!`", "components and props", "graded via HTML output"],
        "Drills use server-side rendering only — no browser required.",
        ["Confusing Leptos components with React — props are Rust values, not JS objects."],
    ),
}


def title_from_dir(d: str) -> str:
    parts = d.split("-", 1)
    return parts[1].replace("-", " ").title() if len(parts) > 1 else d


def generic_snippet(level_dir: str) -> str:
    if level_dir.startswith(("3", "4")) and "axum" in level_dir or level_dir.startswith("31"):
        return ""
    return """```rust
fn main() {
    println!("Type examples from this README into playground with `cargo play`.");
}
```"""


def write_readme(level_dir: str) -> None:
    num = int(level_dir.split("-")[0])
    if num < 17:
        return
    path = LEVELS / level_dir / "README.md"
    if path.exists() and path.stat().st_size > 200:
        return
    if level_dir in EXTRA:
        title, bullets, concept, mistakes = EXTRA[level_dir]
    else:
        title = title_from_dir(level_dir)
        bullets = [f"topics from {title}", "test-driven exercises", "save to grade"]
        concept = f"Work through exercises in order. If this level has dependencies, run `cargo warm {num:02}` first."
        mistakes = ["Skipping compile errors — read them out loud before changing code."]
    learn = "\n".join(f"- {b}" for b in bullets)
    mistakes_md = "\n".join(f"- {m}" for m in mistakes)
    snippet = generic_snippet(level_dir)
    body = f"""# Level {num:02} — {title}

## What you'll learn
{learn}

## Concepts

{concept}

{snippet}

## Common mistakes
{mistakes_md}

## Before you start
Run `cargo warm {num:02}` if this level uses external crates (see `level.toml`). Type examples into `playground` with `cargo play`.

## Exercises
Work through the exercises in order. Save each file to check it.
"""
    path.write_text(body)


def main():
    for d in sorted(LEVELS.iterdir()):
        if d.is_dir() and d.name[0].isdigit():
            write_readme(d.name)
    print("Updated phase READMEs")


if __name__ == "__main__":
    main()
