# Build Spec — Phase 1 (`rust-bootcamp` levels 01–16)

**Give this file to Cursor for Phase 1.** It covers the runner, file conventions, and **200 exercises in levels 01–16**.

Phases 3–6 (levels 17–48, 256 drills) are specified separately in [CURSOR-BUILD-SPEC-PHASES-3-6.md](./CURSOR-BUILD-SPEC-PHASES-3-6.md). The full repo target is **48 levels, 456 auto-graded exercises**.

Read §1–§8 fully before writing code. §9 is the Phase 1 exercise bank. §10 is the build order with acceptance criteria — follow it in sequence.

---

## 1. What we're building

A local Cargo workspace for one learner. She opens an exercise file, writes code, saves. A file watcher immediately builds and runs *that one exercise*, compares its stdout to an expected output, and prints **PASS** or **FAIL** with a diff. When the file doesn't compile — which in Rust is most saves — it prints the compiler's own diagnostic instead. Progress is tracked in a JSON file.

**Non-goals:** no web UI, no server, no database, no accounts, no deployment. This is a terminal experience. Keep it small and fast.

### Why a custom watcher instead of `cargo watch`

`cargo watch` re-runs one fixed command on any change. We need to build and run *the specific exercise that changed*, compare its output, and grade it. That's a few hundred lines with `notify`. `cargo-watch` is not a dependency.

### The measured budget

These numbers come from a real one-file, zero-dependency bin target on the reference machine (Rust 1.90, macOS, `debug = 0`):

| Action | Time |
|---|---|
| `cargo build --bin X` after editing X | **~205 ms** |
| `cargo build --bin X` with nothing changed | **~65 ms** |
| Running the resulting binary | **< 5 ms** |

So a full save → verdict cycle lands in roughly **250 ms**. Every design decision in §5 and §7 exists to protect that number. If it ever exceeds 600 ms, something in §7 has been broken.

---

## 2. Tech constraints

- **Rust 1.90+**, **edition 2024**, `resolver = "3"`. Pin with a `rust-toolchain.toml` (`channel = "1.90"`, components `rustfmt`, `clippy`).
- **Stable Rust only.** No nightly features, no `-Z` flags. The learner must never be blocked on a toolchain upgrade.
- **Exercise and solution crates have zero dependencies.** `std` only. This is the single biggest contributor to the 205 ms rebuild. Level 16 is the only partial exception and it still uses `std` alone.
- **Runner dependencies** (compiled once, then cached): `notify`, `notify-debouncer-full`, `serde` (with `derive`), `serde_json`, `toml`, `owo-colors`, `walkdir`, `sha2`, `anyhow`. Nothing else. No diffing crate — the two-column diff in §5.3 is hand-rolled.
- **Cross-platform:** must work on Windows, macOS, Linux. Use `std::path::Path`/`PathBuf` everywhere, never hardcode `/`. Normalise `\r\n` on read.

---

## 3. Repo structure

```
rust-bootcamp/
├── Cargo.toml                   # workspace root
├── Cargo.lock
├── rust-toolchain.toml
├── config.toml                  # runner settings
├── progress.json                # generated, gitignored
├── checks.lock                  # sha-256 of every check file
├── README.md                    # how to run it, written for a beginner
├── NOTES.md                     # her scratch notes (starts with a template)
├── .gitignore
│
├── .cargo/
│   └── config.toml              # cargo aliases: dev, grade, progress, solution, …
│
├── runner/
│   ├── Cargo.toml
│   └── src/
│       ├── lib.rs
│       ├── bin/
│       │   ├── watch.rs         # notify watcher — the main entry point
│       │   └── cli.rs           # argument parsing for grade / progress / solution / reset
│       ├── build.rs             # cargo build + JSON diagnostic parsing
│       ├── run_one.rs           # build, execute, grade a single exercise
│       ├── grade.rs             # output normalisation + comparison + diff
│       ├── report.rs            # all terminal formatting/colour
│       ├── progress.rs          # read/write progress.json
│       ├── resolve.rs           # id <-> path helpers, level listing
│       ├── config.rs            # config.toml
│       └── gen.rs               # gen-expected + verify-level
│
├── levels/
│   ├── 01-print-and-variables/
│   │   ├── Cargo.toml           # package "level-01-print-and-variables"
│   │   ├── README.md            # concept notes for this level
│   │   ├── hints.toml           # optional per-exercise hints
│   │   ├── src/bin/
│   │   │   ├── 01-hello.rs      # her file — stub with instructions in a doc comment
│   │   │   ├── 02-name-age.rs
│   │   │   └── …
│   │   └── expected/
│   │       ├── 01-hello.txt
│   │       ├── 02-name-age.txt
│   │       └── …
│   ├── 02-operators/
│   └── … through 16-modules-errors-io/
│
├── solutions/                   # reference solutions, one crate per level
│   ├── 01-print-and-variables/
│   │   ├── Cargo.toml           # package "sol-01-print-and-variables"
│   │   └── src/bin/01-hello.rs
│   └── …
│
└── playground/
    ├── Cargo.toml
    └── src/main.rs              # free space, never graded
```

Levels that have test-graded exercises also get a `checks/` directory:

```
levels/08-functions/
├── checks/
│   ├── 01-add.rs                # the test module — she must not edit this
│   └── …
└── src/bin/01-add.rs
```

`checks/` is deliberately **not** named `tests/`. Cargo auto-discovers `tests/` as integration-test targets, which would try to compile these files standalone and fail. `checks/` is invisible to Cargo and is pulled in only through the `#[path]` attribute in §5.5.

### 3.1 Workspace root `Cargo.toml`

```toml
[workspace]
resolver = "3"
members  = ["runner", "playground", "levels/*", "solutions/*"]
default-members = ["runner"]

[workspace.package]
edition = "2024"
version = "0.0.0"
publish = false

[profile.dev]
debug       = 0      # no debuginfo → much faster linking
incremental = true
opt-level   = 0
```

`debug = 0` is safe: panic messages still report the file and line, because `#[track_caller]` location data is baked into the panic call itself and does not come from debuginfo. We never show backtraces, so nothing is lost and linking gets noticeably faster.

`default-members = ["runner"]` means a bare `cargo build` builds only the runner, not 200 exercises.

### 3.2 A level `Cargo.toml`

```toml
[package]
name    = "level-04-for-loops"
edition.workspace = true
version.workspace = true
publish.workspace = true

[dependencies]
```

No dependencies, ever. Bin targets are auto-discovered from `src/bin/*.rs`.

### 3.3 `.cargo/config.toml`

```toml
[alias]
dev          = ["run", "--release", "-p", "runner", "--bin", "watch", "--"]
grade        = ["run", "--release", "-p", "runner", "--bin", "cli", "--", "grade"]
grade-level  = ["run", "--release", "-p", "runner", "--bin", "cli", "--", "grade-level"]
progress     = ["run", "--release", "-p", "runner", "--bin", "cli", "--", "progress"]
solution     = ["run", "--release", "-p", "runner", "--bin", "cli", "--", "solution"]
reset        = ["run", "--release", "-p", "runner", "--bin", "cli", "--", "reset"]
reset-checks = ["run", "--release", "-p", "runner", "--bin", "cli", "--", "reset-checks"]
gen-expected = ["run", "--release", "-p", "runner", "--bin", "cli", "--", "gen-expected"]
verify       = ["run", "--release", "-p", "runner", "--bin", "cli", "--", "verify"]
verify-readmes = ["run", "--release", "-p", "runner", "--bin", "cli", "--", "verify-readmes"]
play         = ["run", "-p", "playground"]
```

Cargo aliases cannot shadow built-in subcommands, which is why these are `grade` and `grade-level` rather than `check` and `test`. The runner is built in release mode once; afterwards `cargo dev` starts in well under a second.

### 3.4 Naming rules

- Level folder: `NN-kebab-case-name`, `NN` zero-padded from `01`. Package name: `level-NN-kebab-case-name`.
- Exercise file: `src/bin/NN-kebab-case-name.rs`, `NN` zero-padded, unique within its level. Cargo accepts bin names that begin with a digit — this is verified, not assumed.
- **Exercise ID** = `<level-folder>/<exercise-basename>`, e.g. `04-for-loops/07-count-digits`. This ID is used in the CLI, in `progress.json`, and in solution lookup.
- Expected output: `expected/<basename>.txt`.
- Test-graded exercises: `checks/<basename>.rs`.
- Solution crate: `sol-NN-kebab-case-name`, same bin basenames as the level.

---

## 4. Exercise file format

Every exercise stub follows this shape exactly:

```rust
//! 04-for-loops / 07-count-digits
//!
//! TASK
//! Count how many digits the number below has, and print the count.
//! Use a loop. Do not turn the number into text.
//!
//! DO NOT CHANGE the GIVEN values.
//!
//! EXPECTED OUTPUT
//! 5

fn main() {
    // ---- GIVEN ----
    let n: u32 = 74821;
    // ---------------

    // Your code below
}
```

Rules for stubs:

- The `TASK` block is one to three plain sentences. No jargon she hasn't met yet.
- `GIVEN` values are always literal constants inside the marked block, with an explicit type annotation wherever the type isn't obvious. **No stdin anywhere in this repo** — reading input makes grading flaky and adds nothing pedagogically at this stage.
- `EXPECTED OUTPUT` is repeated in the doc comment for short outputs (≤ 6 lines) so she doesn't have to open another file. For longer outputs, write `See expected/07-count-digits.txt`.
- Never leave a partial solution in the stub. The body below `// Your code below` is empty.
- An empty stub will emit `warning: unused variable: n`. That is expected and the runner suppresses warnings until the exercise passes (§5.4).

### 4.1 Test-graded stubs

```rust
//! 08-functions / 01-add
//!
//! TASK
//! Write a function `add` that takes two i32 values and returns their sum.
//!
//! SIGNATURE
//! fn add(a: i32, b: i32) -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.

fn add(a: i32, b: i32) -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-add.rs"]
mod tests;
```

And `levels/08-functions/checks/01-add.rs`:

```rust
use super::*;

#[test]
fn adds_two_numbers() {
    assert_eq!(add(2, 3), 5);
    assert_eq!(add(-1, 1), 0);
}

#[test]
fn adds_zero() {
    assert_eq!(add(0, 0), 0);
}
```

The `#[path]` is relative to the directory of the file containing it, so `../../checks/01-add.rs` resolves from `levels/08-functions/src/bin/` to `levels/08-functions/checks/`. The matching solution at `solutions/08-functions/src/bin/01-add.rs` includes the **same** file via `#[path = "../../../../levels/08-functions/checks/01-add.rs"]`, so the stub and the solution can never be graded against different tests.

`todo!()` in the stub body is intentional: it type-checks against any return type, so the stub compiles cleanly and the first verdict she sees is a test failure rather than a wall of type errors.

---

## 5. Grading

### 5.1 The pipeline

Never shell out to `cargo run`. Build and execute are two separate steps, which gives precise diagnostics, an exact timeout, and clean stdout/stderr separation.

**Step 1 — build.**

```
cargo build
  --manifest-path <root>/Cargo.toml
  -p level-04-for-loops
  --bin 07-count-digits
  --message-format=json-diagnostic-rendered-ansi
```

with environment:

| Variable | Value | Why |
|---|---|---|
| `CARGO_TARGET_DIR` | `<root>/target/exercises` | Keeps exercise artifacts out of the runner's own `target/`. Without this, the runner (itself launched by `cargo run`) and the nested build can contend for Cargo's package-cache lock. |
| `CARGO_TERM_COLOR` | `always` | So the rendered diagnostics carry ANSI colour. |

**Step 2 — parse the NDJSON on stdout.** Each line is one JSON object:

- `reason == "compiler-message"` and `message.level == "error"` → collect `message.rendered`. This string is already fully formatted and coloured by rustc; print it as-is.
- `reason == "compiler-message"` and `message.level == "warning"` → collect separately (see §5.4).
- `reason == "compiler-artifact"`, `target.name == "07-count-digits"`, `executable != null` → this is the path to run.

If any errors were collected → status `CompileError`. Stop here.

**Step 3 — execute** the `executable` path directly as a child process:

- `current_dir` = `levels/04-for-loops/` — **always the level crate directory**, so exercises that touch files (level 16) can use short relative paths like `data/sample.txt`.
- Timeout from `config.toml` (default 5000 ms). On timeout, kill the process group and report `Timeout` with the reason `Timed out — you may have an infinite loop.`
- Non-zero exit or any stderr content → `Runtime` error status.

**Step 4 — compare.** Normalise both sides, compare, and diff on mismatch.

### 5.2 Compile-error presentation

This is the verdict she'll see most often, so it matters more than the diff.

```
✗ DOESN'T COMPILE  09-ownership-and-borrowing/01-move

error[E0382]: borrow of moved value: `s1`
 --> src/bin/01-move.rs:4:16
  |
2 |     let s1 = String::from("hello");
  |         -- move occurs because `s1` has type `String`, which does not implement the `Copy` trait
3 |     let s2 = s1;
  |              -- value moved here
4 |     println!("{s1}");
  |                ^^ value borrowed here after move
  |
help: consider cloning the value if the performance cost is acceptable
  |
3 |     let s2 = s1.clone();
  |                ++++++++

  This is normal. Read the arrows: they show where the value moved and where
  you tried to use it afterwards.  `rustc --explain E0382` has a longer
  write-up with worked examples.
```

Rules:

- Print `message.rendered` verbatim, colours included. Do not re-wrap it, do not re-indent it, do not summarise it. rustc's formatting is better than anything we'd write.
- **Strip two kinds of noise:** any `note:` line containing `this error originates in the macro`, and rustc's trailing `For more information about this error, try \`rustc --explain EXXXX\`` footer (which arrives as a separate message with `level == "failure-note"`). Replace the latter with the one-line pointer shown above.
- Cap at the **first 3 errors**. Beginners cascade: one real mistake produces six messages. Append `… and N more errors — fix the first one and most of these will go away.`
- `CompileError` **does not increment the failed-attempt counter** used by the solution lock (§6.5). In Rust, failing to compile is the normal state of writing code; counting it would unlock solutions within minutes.

### 5.3 Output grading and the diff

Normalisation, applied to both actual and expected:

```rust
pub fn normalize(s: &str) -> String {
    s.replace("\r\n", "\n")
        .lines()
        .map(str::trim_end)              // strip trailing whitespace per line
        .collect::<Vec<_>>()
        .join("\n")
        .trim_end()                      // strip trailing blank lines
        .to_string()
}
```

Equal → `Pass`. Otherwise show a line-aligned comparison, capped at 20 lines, with the first differing line marked:

```
✗ FAIL  04-for-loops/12-fibonacci

  line  expected          your output
  ────  ────────────────  ────────────────
   1    0                 0
   2    1                 1
   3    1                 1
   4    2                 3      ← first difference
   5    3                 5
   6    5                 (nothing)

  Hint: check your loop's starting values.
```

The `Hint` line comes from `levels/<level>/hints.toml`:

```toml
"12-fibonacci" = "check your loop's starting values."
```

Omit the line entirely if there's no hint for that exercise.

### 5.4 Warnings

Warnings are shown **only on a PASS**, and never more than two:

```
✓ PASS  11-vectors-and-slices/04-sum-average   (231ms)
        Level 11 — 4/16 done

  Two things the compiler would like you to know:
  warning: unused variable: `total`
  warning: variable does not need to be mutable
```

Showing warnings next to a compile error buries the error. Showing them next to a pass turns them into a free lesson.

If `clippy_hints = true` in `config.toml`, additionally run `cargo clippy -p <level> --bin <name> --message-format=json` after a pass and show at most two clippy suggestions in the same block. Default is `false` — turn it on from level 12.

### 5.5 Test grading

If `levels/<level>/checks/<basename>.rs` exists, the exercise is test-graded and has no `expected/` file.

**Build:**

```
cargo test --manifest-path <root>/Cargo.toml -p level-08-functions --bin 01-add --no-run
  --message-format=json-diagnostic-rendered-ansi
```

Take the `compiler-artifact` whose `target.name == "01-add"` and `profile.test == true`; its `executable` is the test binary.

**Run** that binary directly with `--test-threads=1`, cwd set as in §5.1. Parse its stdout:

- `test tests::adds_two_numbers ... ok` → that check passed
- `test tests::adds_zero ... FAILED` → that check failed
- `test result: ok. 3 passed; 0 failed;` → overall pass
- The `failures:` section carries the panic message — this is what to show

Presentation on failure, in her language rather than libtest's:

```
✗ FAIL  08-functions/01-add

  ✓ adds_zero
  ✗ adds_two_numbers
      you returned 6, the check expected 5
      (assertion `left == right` failed
        left: 6
       right: 5)

  2 checks, 1 passed, 1 failed.
```

Do not use `--format json`; it requires nightly. The plain-text format above is stable.

### 5.6 Check-file tamper protection

`checks.lock` stores the SHA-256 of every file under `levels/*/checks/`. Before grading a test-graded exercise, the runner compares the hash. If it differs:

```
⚠  The checks for 08-functions/01-add have been edited.

   Those are the thing being graded — changing them doesn't change whether
   your code is right. Run `cargo reset-checks 08-functions/01-add` to put
   them back, then try again.
```

and refuses to grade. `cargo reset-checks` restores from `.checks-backup/`, which is written at scaffold time and gitignored only in the sense that it is maintainer-owned.

### 5.7 Generating expected outputs

**Do not hand-write `expected/*.txt` files.** For each output-graded exercise:

1. Write a correct reference solution in `solutions/<level>/src/bin/<name>.rs`.
2. Build and run it, with `current_dir` set to `levels/<level>/` exactly as in §5.1.
3. Write its stdout verbatim to `levels/<level>/expected/<name>.txt`.

This is `cargo gen-expected`, and it regenerates all of them. It guarantees the expected output and the reference solution can never drift apart. Run it as the final build step and commit the results.

If a reference solution fails to compile, errors at runtime, or produces empty output, fail the generation loudly with the exercise ID — do not write an empty expected file.

`cargo verify` is the counterpart: it grades every solution against every expected file and every check file, and must report 200/200.

---

## 6. The runner

### 6.1 `runner/src/bin/watch.rs`

Watch `levels/**/src/bin/*.rs` with `notify` + `notify-debouncer-full` (120 ms debounce — editors write in bursts and an undebounced watcher grades a half-written file). Ignore `target/**` and `**/expected/**`.

```rust
fn main() -> anyhow::Result<()> {
    let root = find_workspace_root()?;
    let cfg = Config::load(&root)?;
    report::banner(&cfg);

    let (tx, rx) = std::sync::mpsc::channel();
    let mut debouncer = new_debouncer(Duration::from_millis(120), None, tx)?;
    debouncer.watch(&root.join("levels"), RecursiveMode::Recursive)?;

    for events in rx {
        for path in changed_rust_files(events?) {
            let Some(id) = resolve::id_from_path(&root, &path) else { continue };

            if cfg.strict_progression {
                if let Some(blocker) = progress::first_unfinished_before(&root, &id)? {
                    report::progression_blocked(&id, &blocker);
                    continue;
                }
            }

            let outcome = run_one::run(&root, &cfg, &id)?;
            progress::record(&root, &outcome)?;
            report::result(&cfg, &outcome, &progress::level_summary(&root, &outcome.level)?);
        }
    }
    Ok(())
}
```

Behaviour requirements:

- **Serialise runs.** Drop (don't queue) saves that arrive while a run is in flight; grade the latest state once the current run finishes.
- **Level 16 non-bin files.** Saving `levels/16-modules-errors-io/src/lib.rs` or `src/math.rs` is not itself an exercise. Re-run the most recently graded exercise in that level instead, so that writing a module and then saving it still produces an instant verdict.
- `strict_progression` means the watcher refuses to grade an exercise in level `N` until level `N-1` is fully green — it prints a short message pointing at the first unfinished exercise instead. This is deliberate; it stops level-skipping.

### 6.2 `runner/src/run_one.rs`

Exports `run(root, cfg, id) -> Outcome`.

```rust
pub enum Status { Pass, Fail, CompileError, Runtime, Timeout, MissingExpected }
pub enum Mode   { Output, Checks }

pub struct Outcome {
    pub id: String,                  // "04-for-loops/07-count-digits"
    pub level: String,               // "04-for-loops"
    pub name: String,                // "07-count-digits"
    pub status: Status,
    pub mode: Mode,
    pub expected: String,
    pub actual: String,
    pub stderr: String,
    pub diagnostics: Vec<String>,    // rendered rustc errors
    pub warnings: Vec<String>,
    pub checks: Vec<CheckResult>,    // populated in Mode::Checks
    pub build_ms: u128,
    pub run_ms: u128,
    pub hint: Option<String>,
}
```

Use `std::process::Command` with piped stdio, and a timeout implemented by spawning a reader thread and `wait_timeout`-style polling — not `output()`, which blocks forever. Kill with `SIGKILL` on Unix / `TerminateProcess` on Windows.

### 6.3 `runner/src/report.rs`

All colour lives here. Requirements:

- Clear the terminal before each result so the screen only ever shows the latest verdict (`print!("\x1B[2J\x1B[H")`, gated on `config.clear_screen`).
- `PASS` in green with a checkmark, the exercise ID, and elapsed time (build + run, reported separately when the build dominated).
- On a pass, show the level's progress: `Level 04 — 7/14 done`.
- When a level goes fully green, print a distinct celebration block and the name of the next level.
- Never print more than 20 diff lines; truncate with `… N more lines`.
- Compile errors are passed through verbatim per §5.2.
- No emoji spam. One glyph per verdict.

### 6.4 `runner/src/progress.rs`

`progress.json` shape:

```json
{
  "version": 1,
  "startedAt": "2026-10-02T10:00:00.000Z",
  "exercises": {
    "04-for-loops/07-count-digits": {
      "status": "pass",
      "attempts": 4,
      "compileErrors": 11,
      "firstPassAt": "2026-10-04T14:22:11.000Z",
      "lastRunAt": "2026-10-04T14:22:11.000Z",
      "solutionViewed": false
    }
  }
}
```

`attempts` counts only `Fail` and `Runtime` outcomes. `compileErrors` is tracked separately and is never used by the solution lock — it's there so you can see at a glance which concepts fought back hardest.

Write atomically (temp file in the same directory + `fs::rename`). Never lose progress on a crash. If the file is corrupt, back it up to `progress.json.bak` and start fresh with a warning rather than panicking.

### 6.5 CLI commands

| Command | Behaviour |
|---|---|
| `cargo dev` | Start the watcher. This is the one she uses all day. |
| `cargo grade <id>` | Run one exercise once and print the verdict. |
| `cargo grade-level <NN>` | Run every exercise in a level, print a summary table. |
| `cargo progress` | Print a dashboard: per-level bar, total done, current level, longest-stuck exercise, total compile errors survived. |
| `cargo solution <id>` | Print the reference solution. **Locked** until the exercise has ≥ 3 recorded failed attempts (compile errors don't count). If locked, print how many attempts remain. `--force` overrides. Sets `solutionViewed: true`. |
| `cargo reset <id\|level>` | Clear an exercise or level's progress and restore the stub. Asks for confirmation. |
| `cargo reset-checks <id>` | Restore tampered check files from `.checks-backup/`. |
| `cargo gen-expected` | Regenerate all `expected/*.txt` from `solutions/`. Maintainer command. |
| `cargo verify` | Grade every solution against every expected file and check file. Must be 200/200. Accepts `--level NN`. Maintainer command. |
| `cargo verify-readmes` | Extract fenced `rust` blocks from every level README and compile them. Maintainer command. |
| `cargo play` | Run `playground/src/main.rs`. Never graded. |

### 6.6 `config.toml`

```toml
clear_screen                   = true
timeout_ms                     = 5000
strict_progression             = true
solution_unlock_after_failures = 3
show_warnings_on_pass          = true
clippy_hints                   = false
max_errors_shown               = 3
```

---

## 7. Protecting the 250 ms loop

Treat these as requirements, not optimisations. Each one is load-bearing.

1. **Zero dependencies in level and solution crates.** One third-party crate in a level's `Cargo.toml` turns a 205 ms rebuild into a multi-second one the first time and adds link time forever after.
2. **`debug = 0` in `[profile.dev]`.** Linking dominates the build of a tiny binary; debuginfo is the bulk of what's being linked. Panic line numbers survive this (see §3.1).
3. **`CARGO_TARGET_DIR=target/exercises` for every nested build.** Prevents package-cache lock contention with the `cargo run`-launched runner, which would otherwise show up as random multi-second stalls.
4. **Build and run as separate steps.** `cargo run` adds its own process layer and interleaves cargo's chatter with the program's stdout. §5.1 avoids both.
5. **Build exactly one bin.** Always pass both `-p <level>` and `--bin <name>`. Never let cargo build a whole level, let alone the workspace.
6. **Debounce at 120 ms, and never queue.** A queued backlog of saves is how a fast runner starts feeling slow.
7. **Runner in `--release`, built once.** A debug-mode runner spends more time starting up than the exercise spends compiling.
8. **Report build and run time separately when the build exceeds 400 ms.** If the loop ever degrades, the numbers on screen should say why without anyone having to profile it.

---

## 8. Level `README.md` template

Every level folder gets one. Cursor drafts it; it must be beginner-readable — short sentences, no unexplained terminology, every concept shown with a runnable snippet.

````md
# Level 04 — For loops

## What you'll learn
- (3–5 bullets, plain language)

## Concepts

### Ranges and `for`
(2–3 sentences of explanation)

```rust
for i in 1..=3 {
    println!("{i}");
}
// 1
// 2
// 3
```
(one sentence on what `1..=3` means, and how it differs from `1..3`)

### ... (one section per concept)

## Common mistakes
- (3–4 real beginner mistakes with the fix, each with the `error[EXXXX]` code
  the compiler will actually show her)

## Before you start
Type every example above into `playground/src/main.rs` and run it with
`cargo play`. Change a number and predict what happens before you run it again.

## Exercises
Work through `01-` to `14-` in order. Save each file to check it.
````

Rules for these READMEs:

- Explain `{i}` in a format string the first time it appears. Explain `%` the first time it appears. Explain `&` the first time it appears. Assume nothing.
- Every code block must actually compile and produce the output shown in its comments.
- No forward references to concepts from later levels. In particular, levels 01–08 must not use `String` where `&str` will do, because ownership isn't taught until level 09.
- **Every level from 09 onward lists the specific `error[EXXXX]` codes she's likely to hit**, with a one-sentence translation of each. Rust error codes are the closest thing she has to a search key when stuck.

---

## 9. The exercise bank — 200 exercises

**Column meaning:** `Expected` is the exact stdout, with `\n` shown as `⏎`. Where the output is long or shape-dependent, it says `→ from solution` — generate it via `cargo gen-expected`.

Unless a row says otherwise, every exercise is **output-graded**. Rows marked **[T]** are **test-graded** — the stub defines a named function and a `checks/<name>.rs` accompanies it.

---

### Level 01 — `01-print-and-variables` (12)

| # | File | Task (with GIVEN values) | Expected |
|---|---|---|---|
| 1 | `01-hello` | Print exactly `Hello, World!` | `Hello, World!` |
| 2 | `02-name-age` | GIVEN `name = "Riya"`, `age = 27`. Print `Riya is 27 years old` using an inline format argument: `println!("{name} is {age} years old")`. | `Riya is 27 years old` |
| 3 | `03-two-lines` | Print `Line one` then `Line two` using two separate `println!` calls. | `Line one⏎Line two` |
| 4 | `04-one-print-two-lines` | Print the same two lines using **one** `println!` and `\n`. | `Line one⏎Line two` |
| 5 | `05-mut-reassign` | Declare `let mut count = 10;`. Print it. Reassign to `20`. Print it again. | `10⏎20` |
| 6 | `06-shadowing` | `let x = 5;` print it. Shadow it with `let x = x * 2;` print it. Shadow it again with `let x = "now a word";` print it. | `5⏎10⏎now a word` |
| 7 | `07-integer-limits` | Print `i32::MAX`, `u8::MAX`, `i64::MIN`, one per line. | `2147483647⏎255⏎-9223372036854775808` |
| 8 | `08-concat` | GIVEN `first = "Ada"`, `last = "Lovelace"`. Build the full name with `format!` and print it. | `Ada Lovelace` |
| 9 | `09-address` | Print a 3-line address with a single `println!`: `12 Park Road` / `Bareilly` / `243001`. | `12 Park Road⏎Bareilly⏎243001` |
| 10 | `10-swap` | GIVEN `a = 1`, `b = 2`. Swap them with tuple destructuring `let (a, b) = (b, a);`, then print `a=2 b=1`. | `a=2 b=1` |
| 11 | `11-decimals` | GIVEN `pi = 3.14159`. Print it to 2 decimal places using `{:.2}`. | `3.14` |
| 12 | `12-escapes` | Print exactly `She said "hello" and left.` then on the next line a tab-separated `a	b`. | `She said "hello" and left.⏎a	b` |

---

### Level 02 — `02-operators` (12)

| # | File | Task | Expected |
|---|---|---|---|
| 1 | `01-arithmetic` | GIVEN `a: i32 = 17`, `b: i32 = 5`. Print sum, difference, product, quotient, remainder — one per line. Note that `a / b` is **integer** division. | `22⏎12⏎85⏎3⏎2` |
| 2 | `02-float-divide` | GIVEN `a: f64 = 17.0`, `b: f64 = 5.0`. Print `a / b`. | `3.4` |
| 3 | `03-casting` | GIVEN `a: i32 = 17`, `b: i32 = 5`. Print `a as f64 / b as f64` to 2 decimals, then `3.9_f64 as i32`, then `-3.9_f64 as i32`. | `3.40⏎3⏎-3` |
| 4 | `04-compound` | GIVEN `let mut total = 100;`. Apply `+= 20`, `-= 30`, `*= 2`, `/= 4` in order, printing after each. | `120⏎90⏎180⏎45` |
| 5 | `05-comparison` | Print `1 == 1`, `2 != 2`, `3 < 4`, `5 >= 6`, one per line. | `true⏎false⏎true⏎false` |
| 6 | `06-logical` | GIVEN `a = true`, `b = false`. Print `a && b`, `a \|\| b`, `!a`, `!b`. | `false⏎true⏎false⏎true` |
| 7 | `07-overflow` | GIVEN `a: u8 = 250`. Print `a.checked_add(10)` with `{:?}`, then `a.wrapping_add(10)`, then `a.saturating_add(10)`. | `None⏎4⏎255` |
| 8 | `08-parse` | GIVEN `s = "42"`. Print `format!("{s}8")`, then `s.parse::<i32>().unwrap() + 8`. | `428⏎50` |
| 9 | `09-parse-failure` | GIVEN `s = "abc"`. Print `s.parse::<i32>().is_err()`, then `s.parse::<i32>().unwrap_or(0)`. | `true⏎0` |
| 10 | `10-math-methods` | Print `(-7i32).abs()`, `2i32.pow(10)`, `144f64.sqrt()`, `4.6f64.round()`, `3.max(9).max(2)`. | `7⏎1024⏎12⏎5⏎9` |
| 11 | `11-precedence` | Print `2 + 3 * 4`, then `(2 + 3) * 4`, then `10 - 4 - 3`. | `14⏎20⏎3` |
| 12 | `12-first-last-digit` | GIVEN `n: i32 = 4739`. Print its last digit using `%`, then its first digit using integer division by 1000. | `9⏎4` |

---

### Level 03 — `03-conditionals-and-match` (12)

| # | File | Task | Expected |
|---|---|---|---|
| 1 | `01-sign` | GIVEN `n = -14`. Print `positive`, `negative`, or `zero`. | `negative` |
| 2 | `02-even-odd` | GIVEN `n = 27`. Print `even` or `odd` using `if`/`else`. | `odd` |
| 3 | `03-max-of-two` | GIVEN `a = 34`, `b = 34`. Print the larger, or `equal` if they're the same. | `equal` |
| 4 | `04-max-of-three` | GIVEN `a = 12`, `b = 45`, `c = 45`. Print the largest value. | `45` |
| 5 | `05-leap-year` | GIVEN `year = 2100`. Print `leap` or `not leap` (divisible by 4, but not 100, unless also by 400). | `not leap` |
| 6 | `06-grade` | GIVEN `marks = 73`. Print grade: 90+ `A`, 75+ `B`, 60+ `C`, 40+ `D`, else `F`. | `C` |
| 7 | `07-if-expression` | GIVEN `n = 10`. Assign `let label = if n % 2 == 0 { "even" } else { "odd" };` and print `label`. Rust has no ternary — `if` *is* the expression. | `even` |
| 8 | `08-match-day` | GIVEN `day = 6`. Use `match` to print the weekday name (1 = Monday). Include a `_` arm printing `not a day`. | `Saturday` |
| 9 | `09-match-range` | GIVEN `score = 73`. Redo exercise 6 with `match` and range patterns (`90..=100 => "A"` and so on). | `C` |
| 10 | `10-match-calc` | GIVEN `a = 12`, `b = 4`, `op: char = '/'`. `match` on `op`, handle `+ - * /` and a default. | `3` |
| 11 | `11-can-vote` | GIVEN `age = 17`, `is_citizen = true`. Print `can vote` only if 18+ **and** a citizen, else `cannot vote`. | `cannot vote` |
| 12 | `12-fizzbuzz-one` | GIVEN `n = 15`. Use `match (n % 3, n % 5)` to print `FizzBuzz`, `Fizz`, `Buzz`, or the number. | `FizzBuzz` |

---

### Level 04 — `04-for-loops` (14)

| # | File | Task | Expected |
|---|---|---|---|
| 1 | `01-one-to-ten` | Print 1 to 10, one per line, with `1..=10`. | `1⏎2⏎…⏎10` |
| 2 | `02-ten-to-one` | Print 10 down to 1 using `.rev()`. | `10⏎9⏎…⏎1` |
| 3 | `03-evens` | Print every even number from 2 to 20 using `.step_by(2)`. | → from solution |
| 4 | `04-sum-to-n` | GIVEN `n = 100`. Print the sum of 1 to n with an accumulator. | `5050` |
| 5 | `05-times-table` | GIVEN `n = 7`. Print `7 x 1 = 7` through `7 x 10 = 70`. | → from solution |
| 6 | `06-factorial` | GIVEN `n: u64 = 6`. Print n factorial using a loop. | `720` |
| 7 | `07-count-digits` | GIVEN `n: u32 = 74821`. Print how many digits it has, using a loop (not `.to_string()`). | `5` |
| 8 | `08-reverse-number` | GIVEN `n: u32 = 12345`. Print the number reversed, as a number. | `54321` |
| 9 | `09-power` | GIVEN `base: u64 = 3`, `exp = 5`. Compute `base^exp` with a loop (no `.pow()`). | `243` |
| 10 | `10-sum-of-digits` | GIVEN `n: u32 = 9375`. Print the sum of its digits. | `24` |
| 11 | `11-squares` | Print the square of every number 1 to 8, one per line. | → from solution |
| 12 | `12-fibonacci` | GIVEN `n = 10`. Print the first n Fibonacci numbers starting `0, 1`, one per line. | → from solution |
| 13 | `13-fizzbuzz` | Print FizzBuzz for 1 to 20, one per line. | → from solution |
| 14 | `14-count-vowels` | GIVEN `s = "learning rust is fun"`. Loop over `s.chars()` and print the vowel count. | `6` |

---

### Level 05 — `05-while-and-loop` (10)

| # | File | Task | Expected |
|---|---|---|---|
| 1 | `01-while-count` | GIVEN `n = 5`. Print 1 to n using a `while` loop. | `1⏎2⏎3⏎4⏎5` |
| 2 | `02-sum-digits-while` | GIVEN `n: u32 = 48291`. Print the digit sum using `while`. | `24` |
| 3 | `03-reverse-while` | GIVEN `n: u32 = 9081`. Print it reversed using `while`. | `1809` |
| 4 | `04-palindrome-number` | GIVEN `n: u32 = 12321`. Print `palindrome` or `not palindrome`. | `palindrome` |
| 5 | `05-armstrong` | GIVEN `n: u32 = 153`. Print `armstrong` if the sum of each digit cubed equals n. | `armstrong` |
| 6 | `06-gcd` | GIVEN `a = 48`, `b = 18`. Print the GCD using Euclid's algorithm with `while`. | `6` |
| 7 | `07-to-binary` | GIVEN `n: u32 = 25`. Print its binary form by repeatedly dividing by 2 (no `{:b}`). | `11001` |
| 8 | `08-loop-break-value` | Use `loop` with a counter. `break` out **returning** the first number whose square exceeds 50, assign it to a variable, and print it. | `8` |
| 9 | `09-labeled-break` | Two nested loops over `1..=5`. Find the first pair whose product is 12 and use a labelled `break 'outer` to stop both. Print `3 4`. | `3 4` |
| 10 | `10-collatz` | GIVEN `n: u64 = 27`. Count the steps to reach 1 (even → n/2, odd → 3n+1). Print the count. | `111` |

---

### Level 06 — `06-patterns` (16)

All patterns use GIVEN `n = 5` unless noted. Every expected output comes from the reference solution. These map directly to Striver Step 1, Lec 2.

| # | File | Pattern |
|---|---|---|
| 1 | `01-star-square` | 5×5 solid square of `*` |
| 2 | `02-star-triangle` | Left-aligned right triangle of `*`, rows 1→5 |
| 3 | `03-number-triangle` | Left-aligned triangle where row `i` prints `1 2 … i` |
| 4 | `04-same-number-triangle` | Row `i` prints the digit `i` repeated `i` times |
| 5 | `05-inverted-star-triangle` | Left-aligned triangle of `*`, rows 5→1 |
| 6 | `06-inverted-number-triangle` | Rows 5→1, row prints `1 2 … i` |
| 7 | `07-floyds-triangle` | Numbers 1..15 laid out in 5 rows, continuing across rows |
| 8 | `08-binary-triangle` | Triangle of alternating `1`/`0`, each row starting with `1` |
| 9 | `09-pyramid` | Centred pyramid of `*`, 5 rows |
| 10 | `10-inverted-pyramid` | Centred pyramid of `*`, upside down |
| 11 | `11-diamond` | Pyramid on top of inverted pyramid |
| 12 | `12-half-diamond` | Triangle up then triangle down, left-aligned |
| 13 | `13-butterfly` | Butterfly pattern of `*`, `n = 4` |
| 14 | `14-hollow-square` | 5×5 square, `*` on the border, spaces inside |
| 15 | `15-alphabet-triangle` | Row `i` prints `A B … ` up to the `i`-th letter, via `(b'A' + k) as char` |
| 16 | `16-multiplication-grid` | 5×5 multiplication table, each column right-aligned to width 4 with `{:>4}` |

Reference solutions must build each row into a `String` (with `push`, `push_str`, or `"*".repeat(i)`) and print it with **one** `println!` per row. Do not use `print!` or `write!` to stdout. The level README must show this pattern explicitly, and must explain `String::new()` and `push_str` — this is her first contact with an owned, growable value, two levels before ownership is taught properly.

---

### Level 07 — `07-number-problems` (14)

Direct preparation for Striver's "Basic Maths".

| # | File | Task | Expected |
|---|---|---|---|
| 1 | `01-count-digits` | GIVEN `n: u32 = 946213`. Print digit count. | `6` |
| 2 | `02-reverse` | GIVEN `n: u32 = 700`. Print reversed as a number (leading zeros dropped). | `7` |
| 3 | `03-palindrome` | GIVEN `n: u32 = 1221`. Print `true` or `false`. | `true` |
| 4 | `04-armstrong` | GIVEN `n: u32 = 371`. Print `true` or `false`. | `true` |
| 5 | `05-divisors` | GIVEN `n: u32 = 36`. Print all divisors, space-separated, on one line. | `1 2 3 4 6 9 12 18 36` |
| 6 | `06-is-prime` | GIVEN `n: u32 = 97`. Print `prime` or `not prime`. Loop only while `i * i <= n`. | `prime` |
| 7 | `07-gcd` | GIVEN `a = 120`, `b = 45`. Print the GCD. | `15` |
| 8 | `08-lcm` | GIVEN `a = 12`, `b = 18`. Print the LCM using `(a * b) / gcd`. | `36` |
| 9 | `09-sum-divisors` | GIVEN `n: u32 = 28`. Print the sum of all divisors including n. | `56` |
| 10 | `10-perfect-number` | GIVEN `n: u32 = 496`. Print `perfect` if its proper divisors sum to n. | `perfect` |
| 11 | `11-prime-factors` | GIVEN `n: u32 = 360`. Print prime factors with repeats, space-separated. | `2 2 2 3 3 5` |
| 12 | `12-primes-to-n` | GIVEN `n: u32 = 30`. Print every prime from 2 to n, space-separated. | `2 3 5 7 11 13 17 19 23 29` |
| 13 | `13-nth-prime` | GIVEN `k = 20`. Print the 20th prime number. | `71` |
| 14 | `14-digit-frequency` | GIVEN `n: u64 = 1223334444`. Print each distinct digit and its count as `digit:count`, ascending, space-separated. Use a `[u32; 10]` array, not a map. | `1:1 2:2 3:3 4:4` |

---

### Level 08 — `08-functions` (12)

Exercises 1–8 are **[T]** test-graded. Exercises 9–12 are output-graded because they demonstrate behaviour rather than compute a value.

| # | File | Task | Expected |
|---|---|---|---|
| 1 | `01-add` **[T]** | `fn add(a: i32, b: i32) -> i32` returning their sum. | checks |
| 2 | `02-expression-return` **[T]** | `fn multiply(a: i32, b: i32) -> i32`, written with **no** `return` keyword and no semicolon on the last line. | checks |
| 3 | `03-is-even` **[T]** | `fn is_even(n: i32) -> bool`. | checks |
| 4 | `04-min-max` **[T]** | `fn min_max(numbers: &[i32]) -> (i32, i32)` returning a tuple. Assume non-empty. | checks |
| 5 | `05-greet` **[T]** | `fn greet(name: &str) -> String` returning `"Hello, Ada!"` style. | checks |
| 6 | `06-optional-arg` **[T]** | `fn greet_with(name: &str, greeting: Option<&str>) -> String`. `None` means `"Hello"`. Rust has no default parameters — this is how you get them. | checks |
| 7 | `07-apply-twice` **[T]** | `fn apply_twice(f: impl Fn(i32) -> i32, value: i32) -> i32` returning `f(f(value))`. | checks |
| 8 | `08-make-multiplier` **[T]** | `fn make_multiplier(n: i32) -> impl Fn(i32) -> i32`. | checks |
| 9 | `09-unit-return` | Define `fn five() -> i32` and `fn log_five()` (no return type). Print `five()`, then call `log_five()`, then print its result with `{:?}`. | `5⏎5⏎()` |
| 10 | `10-early-return` | `fn classify(n: i32) -> &'static str` using early `return` for the negative and zero cases. Call with `-5`, `0`, `7` and print each. | `negative⏎zero⏎positive` |
| 11 | `11-callback` | `fn repeat(times: u32, f: impl Fn(u32))` that calls `f` with each index `0..times`. Call it with `3` and a closure printing `step 0` etc. | `step 0⏎step 1⏎step 2` |
| 12 | `12-block-expression` | `let x = { let a = 3; let b = 4; a * b };` print `x`. Then inside a new `{ }` block shadow a variable to `"inner"`, print it, and print the outer value `"outer"` after the block closes. | `12⏎inner⏎outer` |

---

### Level 09 — `09-ownership-and-borrowing` (12)

**This is the level everything after it depends on.** Budget four days. Every stub's doc comment must name the `error[EXXXX]` code she would see if she got it wrong, and the README must list `E0382` (use after move), `E0502` (mutable + immutable borrow), `E0499` (two mutable borrows), `E0505` (move out of borrowed value), `E0106` (missing lifetime) with a one-line translation of each.

| # | File | Task | Expected |
|---|---|---|---|
| 1 | `01-move` | GIVEN `let s1 = String::from("hello");`. Write `let s2 = s1;` and print `s2`. Then add a comment explaining, in your own words, why printing `s1` here would be `E0382`. | `hello` |
| 2 | `02-clone` | Same start, but `let s2 = s1.clone();`. Print both. Comment on what `clone` actually cost. | `hello⏎hello` |
| 3 | `03-copy-types` | GIVEN `let a = 5; let b = a;`. Print both. Comment on why this works when the `String` version didn't — `i32` is `Copy`. | `5⏎5` |
| 4 | `04-borrow` | Write `fn length(s: &String) -> usize`. Call it on an owned `String`, print the length, then print the original `String` — proving a borrow didn't consume it. | `5⏎hello` |
| 5 | `05-mutable-borrow` | Write `fn add_excl(s: &mut String)` that pushes `'!'`. Call it and print the result. | `hello!` |
| 6 | `06-borrow-scopes` | Call `add_excl` twice in sequence, printing in between. Comment on why the two `&mut` borrows are fine sequentially but would be `E0499` simultaneously. | `hello!⏎hello!!` |
| 7 | `07-ownership-round-trip` | Write `fn consume(s: String) -> (usize, String)` returning the length **and** the string back. Use it, then print the length and the still-usable string. | `5⏎hello` |
| 8 | `08-slices` | GIVEN `let s = String::from("hello world");`. Print `&s[0..5]` and `&s[6..]`. | `hello⏎world` |
| 9 | `09-first-word` **[T]** | `fn first_word(s: &str) -> &str` returning everything up to the first space, or the whole string. Note the returned `&str` borrows from the input — that's why no lifetime annotation is needed. | checks |
| 10 | `10-slice-param` | GIVEN `let v = vec![1, 2, 3];`. Write `fn total(v: &[i32]) -> i32`. Call it, print the total, then print `v` joined by spaces — proving `&[i32]` borrowed rather than moved. | `6⏎1 2 3` |
| 11 | `11-shadow-vs-mut` | `let mut x = 5;` print, `x = 6;` print, then shadow with `let x = "six";` and print. Comment on the difference between reassigning and shadowing. | `5⏎6⏎six` |
| 12 | `12-return-owned` | Write `fn make_greeting(name: &str) -> String` that builds and returns an owned `String`. Comment on why returning `&str` built from a local would be `E0106`/`E0515`. | `Hello, Ada!` |

---

### Level 10 — `10-strings` (14)

| # | File | Task | Expected |
|---|---|---|---|
| 1 | `01-str-vs-string` | GIVEN `let a: &str = "rust";` and `let b: String = String::from("rust");`. Print `a`, print `b`, print `b == a`. | `rust⏎rust⏎true` |
| 2 | `02-basics` | GIVEN `s = "Rustacean"`. Print `s.len()`, uppercase, lowercase. | `9⏎RUSTACEAN⏎rustacean` |
| 3 | `03-loop-chars` | GIVEN `s = "code"`. Print each character on its own line with `.chars()`. | `c⏎o⏎d⏎e` |
| 4 | `04-reverse` | GIVEN `s = "bareilly"`. Print it reversed using `.chars().rev()`. | `yllierab` |
| 5 | `05-palindrome` | GIVEN `s = "racecar"`. Print `true` or `false`. | `true` |
| 6 | `06-count-vowels-consonants` | GIVEN `s = "hello world"`. Print `vowels: 3` then `consonants: 7`. | `vowels: 3⏎consonants: 7` |
| 7 | `07-word-count` | GIVEN `s = " the quick  brown fox "`. Print the word count with `split_whitespace`. | `4` |
| 8 | `08-title-case` | GIVEN `s = "learning rust today"`. Print it with each word capitalised. | `Learning Rust Today` |
| 9 | `09-remove-duplicates` | GIVEN `s = "programming"`. Print the string with duplicate characters removed, keeping first occurrences. | `progamin` |
| 10 | `10-split-join` | GIVEN `s = "a,b,c,d"`. Split on `','` into a `Vec<&str>` and print it joined by `" - "`. | `a - b - c - d` |
| 11 | `11-search-methods` | GIVEN `s = "rustlang"`. Print `s.contains("lang")`, `s.starts_with("rust")`, `s.ends_with("x")`, and `s.find('t')` with `{:?}`. | `true⏎true⏎false⏎Some(3)` |
| 12 | `12-slice-and-get` | GIVEN `s = "abcdefgh"`. Print `&s[2..5]`, `&s[5..]`, and `s.get(2..5)` with `{:?}`. The README must explain why slicing is by **byte** index and what happens with a non-ASCII string. | `cde⏎fgh⏎Some("cde")` |
| 13 | `13-replace-trim-pad` | GIVEN `s = "cat bat cat"`. Print `s.replace("cat", "dog")`, then `s.replacen("cat", "dog", 1)`. Then GIVEN `t = "  7  "`, print `t.trim()` and `format!("{:0>5}", t.trim())`. | `dog bat dog⏎dog bat cat⏎7⏎00007` |
| 14 | `14-anagram` | GIVEN `a = "listen"`, `b = "silent"`. Print `true` if they're anagrams, by sorting each one's chars into a `Vec<char>` and comparing. | `true` |

---

### Level 11 — `11-vectors-and-slices` (16)

Every exercise prints its result. Vectors are printed by mapping to `String` and joining with `" "` unless stated, so output is a clean single line.

| # | File | Task | Expected |
|---|---|---|---|
| 1 | `01-basics` | GIVEN `v = vec![10, 20, 30]`. Print `v.len()`, `v[0]`, and the last element. | `3⏎10⏎30` |
| 2 | `02-mutate` | GIVEN `let mut v = vec![2, 3];`. `push(4)`, `insert(0, 1)`, print joined. Then `pop()`, `remove(0)`, print joined. | `1 2 3 4⏎2 3` |
| 3 | `03-two-loops` | GIVEN `v = vec!["a", "b", "c"]`. Print each element with an index loop, then again with `for x in &v`. | `a⏎b⏎c⏎a⏎b⏎c` |
| 4 | `04-sum-average` | GIVEN `v = vec![4, 8, 15, 16, 23, 42]`. Print the sum, then the average to 2 decimals. | `108⏎18.00` |
| 5 | `05-largest` | GIVEN `v = vec![3, 41, 7, 41, 19]`. Print the largest element without `.max()`. | `41` |
| 6 | `06-second-largest` | GIVEN `v = vec![12, 35, 1, 10, 34, 35]`. Print the second largest **distinct** value. | `34` |
| 7 | `07-is-sorted` | GIVEN `v = vec![1, 2, 2, 5, 9]`. Print `true` if non-decreasing. Write the loop yourself. | `true` |
| 8 | `08-reverse-in-place` | GIVEN `let mut v = vec![1, 2, 3, 4, 5];`. Reverse it with two indices and `v.swap(i, j)`, no `.reverse()`. Print joined. | `5 4 3 2 1` |
| 9 | `09-linear-search` | GIVEN `v = vec![7, 3, 9, 1]`, `target = 9`. Print the index, or `-1` if absent. | `2` |
| 10 | `10-count-occurrences` | GIVEN `v = vec![1, 3, 3, 5, 3]`, `target = 3`. Print how many times it appears. | `3` |
| 11 | `11-remove-duplicates-sorted` | GIVEN `v = vec![1, 1, 2, 2, 2, 3, 3]`. Print the unique values joined. | `1 2 3` |
| 12 | `12-rotate-one` | GIVEN `v = vec![1, 2, 3, 4, 5]`. Left-rotate by one place. Print joined. | `2 3 4 5 1` |
| 13 | `13-rotate-k` | GIVEN `v = vec![1, 2, 3, 4, 5, 6, 7]`, `k = 3`. Left-rotate by k. Print joined. | `4 5 6 7 1 2 3` |
| 14 | `14-move-zeros` | GIVEN `v = vec![0, 1, 0, 3, 12]`. Move all zeros to the end, keeping the order of the rest. Print joined. | `1 3 12 0 0` |
| 15 | `15-union-sorted` | GIVEN `a = vec![1, 2, 3, 4, 6]`, `b = vec![2, 3, 5]`. Print the sorted union, joined. | `1 2 3 4 5 6` |
| 16 | `16-missing-number` | GIVEN `v = vec![0, 1, 2, 4, 5]`, `n = 5`. Print the missing number from `0..=n`. | `3` |

---

### Level 12 — `12-iterators-and-closures` (12)

| # | File | Task | Expected |
|---|---|---|---|
| 1 | `01-for-each` | GIVEN `v = vec![10, 20, 30]`. Use `.iter().enumerate().for_each(…)` to print `index: value`. | `0: 10⏎1: 20⏎2: 30` |
| 2 | `02-map` | GIVEN `v = vec![1, 2, 3, 4]`. Double each element, `collect::<Vec<_>>()`, print joined. | `2 4 6 8` |
| 3 | `03-filter` | GIVEN `1..=10`. Keep only even numbers, collect, print joined. | `2 4 6 8 10` |
| 4 | `04-fold-and-sum` | GIVEN `v = vec![5, 10, 15]`. Print the total with `.fold(0, …)`, then again with `.sum::<i32>()`. | `30⏎30` |
| 5 | `05-max-min` | GIVEN `v = vec![4, 19, 7, 2]`. Print the max and min. Note in a comment that `.max()` returns an `Option` because the iterator might be empty. | `19⏎2` |
| 6 | `06-find-position` | GIVEN `v = vec![3, 8, 12, 5]`. Print `.iter().find(…)` for the first element over 7 and `.iter().position(…)` for its index, both with `{:?}`. | `Some(8)⏎Some(1)` |
| 7 | `07-any-all` | GIVEN `v = vec![2, 4, 6, 7]`. Print `.any(is odd)` then `.all(is even)`. | `true⏎false` |
| 8 | `08-sort` | GIVEN `let mut v = vec![10, 9, 100, 2];`. Print it sorted ascending with `.sort()`, then descending with `.sort_by(|a, b| b.cmp(a))`. Comment on why `.sort()` needs no comparator here, and what `b.cmp(a)` is doing differently. | `2 9 10 100⏎100 10 9 2` |
| 9 | `09-sort-strings` | GIVEN `let mut v = vec!["banana", "apple", "cherry"];`. Print sorted alphabetically, joined. | `apple banana cherry` |
| 10 | `10-chaining` | GIVEN `1..=10`. Keep the evens, square them, sum them. Print the result in one chain. | `220` |
| 11 | `11-closure-capture` | GIVEN `let factor = 3;`. Make a closure `times` that multiplies by `factor`; print `times(5)`. Then make a second closure that captures `factor` by `move` and print `times2(10)`. | `15⏎30` |
| 12 | `12-take-skip-zip` | GIVEN `v = vec![1, 2, 3, 4, 5]`, `letters = vec!["a", "b"]`. Print `.take(2)` joined, `.skip(3)` joined, then `v.iter().zip(letters.iter())` formatted as `1a 2b`. | `1 2⏎4 5⏎1a 2b` |

---

### Level 13 — `13-structs-and-enums` (12)

Shared GIVEN for exercises 6–8 and 11:

```rust
#[derive(Debug)]
struct Person { name: String, age: u32, city: String }

let people = vec![
    Person { name: "Ada".into(),   age: 36, city: "London".into()  },
    Person { name: "Raman".into(), age: 42, city: "Kolkata".into() },
    Person { name: "Meera".into(), age: 29, city: "Pune".into()    },
];
```

| # | File | Task | Expected |
|---|---|---|---|
| 1 | `01-struct-basics` | Define `struct User { name: String, age: u32 }`, build one for Ada/36, print each field. | `Ada⏎36` |
| 2 | `02-derive-debug` | Add `#[derive(Debug)]` to that struct and print the whole thing with `{:?}`. | `User { name: "Ada", age: 36 }` |
| 3 | `03-impl-methods` | `struct Rectangle { width: u32, height: u32 }` with an associated function `new` and a method `area(&self) -> u32`. Build 4×7 and print the area. | `28` |
| 4 | `04-mutate-struct` | `let mut u = User { … };` set `u.age = 37;` and print it. Comment on why the binding needed `mut`. | `37` |
| 5 | `05-nested-struct` | `struct Address { city: String }` inside `struct User`. Build one with city `Bareilly` and print `user.address.city`. | `Bareilly` |
| 6 | `06-list-names` | Use `people`. Print each person's name on its own line. | `Ada⏎Raman⏎Meera` |
| 7 | `07-filter-people` | Use `people`. Print the names of everyone over 30, joined by `", "`. | `Ada, Raman` |
| 8 | `08-sort-people` | Use `people`. Print names sorted by age ascending, joined by a space. | `Meera Ada Raman` |
| 9 | `09-enum-basics` | `enum Direction { North, South, East, West }`. `match` on `Direction::South` and print `going south`. | `going south` |
| 10 | `10-enum-with-data` | `enum Shape { Circle(f64), Rect(f64, f64) }`. Write `fn area(s: &Shape) -> f64` using `match`. Print the area of `Circle(5.0)` then `Rect(3.0, 4.0)`, each to 2 decimals. | `78.54⏎12.00` |
| 11 | `11-option` | Use `people`. Find Ada with `.iter().find(…)` and print her name via `match`. Then search for `"Zara"` and print `none` using the `None` arm. | `Ada⏎none` |
| 12 | `12-result` | `fn divide(a: i32, b: i32) -> Result<i32, String>` returning `Err` when `b == 0`. `match` both outcomes: print the result of `divide(12, 4)` and the error message of `divide(1, 0)`. | `3⏎Cannot divide by zero` |

---

### Level 14 — `14-recursion` (10)

Maps to Striver Step 1, Lec 5. Exercises 4–10 are **[T]** test-graded so she thinks in terms of return values, not printing.

| # | File | Task | Expected |
|---|---|---|---|
| 1 | `01-print-n-times` | Recursively print `learning` 4 times. No loops. | `learning` ×4 |
| 2 | `02-print-one-to-n` | GIVEN `n = 5`. Recursively print 1 to n. | `1⏎2⏎3⏎4⏎5` |
| 3 | `03-print-n-to-one` | GIVEN `n = 5`. Recursively print n down to 1. | `5⏎4⏎3⏎2⏎1` |
| 4 | `04-sum-to-n` **[T]** | `fn sum_to(n: u32) -> u32` returning 1+2+…+n recursively. | checks |
| 5 | `05-factorial` **[T]** | `fn factorial(n: u64) -> u64`. `factorial(0)` must return 1. | checks |
| 6 | `06-reverse-vec` **[T]** | `fn reverse(v: &[i32]) -> Vec<i32>` returning a reversed **new** vector, recursively. | checks |
| 7 | `07-is-palindrome` **[T]** | `fn is_palindrome(s: &str) -> bool` using two indices into `s.as_bytes()`, recursively. | checks |
| 8 | `08-fibonacci` **[T]** | `fn fib(n: u32) -> u64` where `fib(0) = 0`, `fib(1) = 1`. | checks |
| 9 | `09-power` **[T]** | `fn power(base: u64, exp: u32) -> u64` recursively. | checks |
| 10 | `10-sum-digits` **[T]** | `fn sum_digits(n: u64) -> u64` recursively. | checks |

The level README must include a call-stack trace for `factorial(4)` drawn out line by line, and must mention that Rust does **not** guarantee tail-call optimisation — deep recursion overflows the stack, and that is a real constraint, not a bug in her code.

---

### Level 15 — `15-hashmaps-and-sets` (10)

Maps to Striver Step 1, Lec 6.

The README must open with the single most important fact: **`HashMap` iteration order is unspecified and deliberately randomised.** Every exercise here therefore either sorts the output or uses `BTreeMap`. Exercise 3 exists specifically to make that concrete.

| # | File | Task | Expected |
|---|---|---|---|
| 1 | `01-char-count` | GIVEN `s = "banana"`. Count characters into a `HashMap<char, u32>`. Collect the pairs into a `Vec`, sort by character, print `char:count` space-separated. | `a:3 b:1 n:2` |
| 2 | `02-entry-api` | Same output, but build the map with `*map.entry(c).or_insert(0) += 1;`. | `a:3 b:1 n:2` |
| 3 | `03-btreemap-order` | Same output again with a `BTreeMap`, **without** sorting afterwards. Comment on why no sort was needed. | `a:3 b:1 n:2` |
| 4 | `04-value-frequency` | GIVEN `v = vec![10, 5, 10, 15, 10, 5]`. Print `value:count` sorted by value, space-separated. | `5:2 10:3 15:1` |
| 5 | `05-high-low-frequency` | Same vector. Print `highest: 10` then `lowest: 15` (ties broken by the smaller value). | `highest: 10⏎lowest: 15` |
| 6 | `06-hashset-unique` | GIVEN `v = vec![1, 2, 2, 3, 3, 3]`. Print the unique values sorted and joined, then the count. | `1 2 3⏎3` |
| 7 | `07-set-operations` | GIVEN `a = vec![1, 2, 3, 4]`, `b = vec![3, 4, 5]`. Print the union sorted and joined, then the intersection sorted and joined, using `HashSet::union` / `intersection`. | `1 2 3 4 5⏎3 4` |
| 8 | `08-first-non-repeating` | GIVEN `s = "swiss"`. Print the first character that appears exactly once, or `none`. | `w` |
| 9 | `09-two-sum` | GIVEN `v = vec![2, 7, 11, 15]`, `target = 9`. Print the two indices, space-separated, using a `HashMap` in **one** pass. | `0 1` |
| 10 | `10-group-by-letter` | GIVEN `words = ["apple", "avocado", "banana", "blueberry", "cherry"]`. Group by first letter into a `BTreeMap<char, Vec<&str>>` and print `a: apple, avocado` style, one line per letter. | `a: apple, avocado⏎b: banana, blueberry⏎c: cherry` |

---

### Level 16 — `16-modules-errors-io` (12)

The bridge to Phases 3–6. This level's crate is the only one with a `src/lib.rs`, because exercise 2 requires a real multi-file module and a bin target cannot have sibling module files inside `src/bin/` (Cargo would try to compile them as additional binaries).

Scaffolding for this level:

- `levels/16-modules-errors-io/src/lib.rs` — starts with only a comment telling her to add `pub mod` declarations here
- `levels/16-modules-errors-io/data/sample.txt` — contents: `hello from a file`
- `levels/16-modules-errors-io/data/numbers.txt` — contents: `3`, `1`, `4`, `1`, `5`, one per line
- `levels/16-modules-errors-io/data/.gitignore` containing `out.txt`

Because the runner sets the working directory to the level crate (§5.1), exercises reference these as `data/sample.txt`.

| # | File | Task | Expected |
|---|---|---|---|
| 1 | `01-inline-module` | Declare `mod greet { pub fn hello(name: &str) -> String { … } }` inside this file and call it. | `Hello, Ada!` |
| 2 | `02-lib-module` | Create `src/math.rs` with `pub fn add` and `pub fn subtract`, declare `pub mod math;` in `src/lib.rs`, then `use level_16_modules_errors_io::math::{add, subtract};` here. Print `add(5, 3)` then `subtract(5, 3)`. | `8⏎2` |
| 3 | `03-visibility` | In an inline module, write a private `fn secret() -> i32` and a `pub fn reveal()` that calls it. Print `secret: 42`. Comment on the `E0603` you'd get calling `secret` directly. | `secret: 42` |
| 4 | `04-option-combinators` | GIVEN `v = vec![1, 2, 3]`. Print `v.get(1)` and `v.get(9)` with `{:?}`, then `v.get(9).copied().unwrap_or(-1)`, then `v.get(1).map(\|x\| x * 10)` with `{:?}`. | `Some(2)⏎None⏎-1⏎Some(20)` |
| 5 | `05-result-match` | Print `"42".parse::<i32>().unwrap()`, then `match "4x".parse::<i32>()` printing `not a number` on the `Err` arm. | `42⏎not a number` |
| 6 | `06-question-mark` | `fn double(s: &str) -> Result<i32, std::num::ParseIntError>` using `?` on the parse. Call with `"21"` and with `"x"`, printing the doubled value and then `could not parse`. | `42⏎could not parse` |
| 7 | `07-custom-error` | `enum MathError { DivideByZero }` with `impl std::fmt::Display`. `fn checked_div(a: i32, b: i32) -> Result<i32, MathError>`. Print `checked_div(10, 2)` on success and the `Display` text on failure. | `5⏎cannot divide by zero` |
| 8 | `08-expect-vs-result` | Show both styles on the same input: `"42".parse::<i32>().expect("the config value must be a number")` printed, then a `unwrap_or_else` fallback on bad input printing `recovered`. Comment on when a panic is the right call. | `42⏎recovered` |
| 9 | `09-write-file` | Write `hello from a file` to `data/out.txt` with `std::fs::write`, read it back with `std::fs::read_to_string`, print it. | `hello from a file` |
| 10 | `10-read-file` | Read `data/sample.txt` with `std::fs::read_to_string` and print its trimmed contents. | `hello from a file` |
| 11 | `11-read-lines` | Read `data/numbers.txt`, parse each line as `i32`, print the sum. | `14` |
| 12 | `12-main-returns-result` | Write `fn main() -> Result<(), Box<dyn std::error::Error>>` that reads `data/sample.txt` with `?`, prints the trimmed contents, and returns `Ok(())`. | `hello from a file` |

---

## 10. Build order for Cursor

Do these in sequence. Don't start a step until the previous one's acceptance criteria pass.

### Step 1 — Skeleton
Create the workspace root `Cargo.toml` (§3.1), `rust-toolchain.toml`, `.cargo/config.toml` (§3.3), `.gitignore` (`/target`, `progress.json`, `progress.json.bak`), `config.toml`, the empty `runner/` and `levels/` directories, `playground/`, and `NOTES.md` with a template containing `## Confused about`, `## Learned today`, `## Re-solve list`.

**Acceptance:** `cargo build` succeeds and builds only the runner skeleton. `cargo play` prints something.

### Step 2 — Grader core
Implement `runner/src/grade.rs` (normalise, compare, build a diff structure) and `runner/src/resolve.rs` (path ↔ ID, list levels, list exercises in a level, find the first unfinished exercise).

**Acceptance:** unit tests in `runner/src/grade.rs` covering: exact match, trailing whitespace, `\r\n`, trailing newlines, empty actual, actual longer than expected. `cargo test -p runner` is green.

### Step 3 — Build layer
Implement `runner/src/build.rs`: invoke `cargo build` with `--message-format=json-diagnostic-rendered-ansi`, parse the NDJSON, extract rendered errors, warnings, and the `executable` path. Implement the noise filtering and 3-error cap from §5.2.

**Acceptance:** hand-create one exercise with a deliberate `E0382` and confirm the rendered diagnostic is captured, the macro-origin `note:` is stripped, and the executable path is `None`. Fix it and confirm the executable path is returned.

### Step 4 — Single-run + reporting
Implement `runner/src/run_one.rs` and `runner/src/report.rs`. Build the two-column diff renderer.

**Acceptance:** hand-create `01-print-and-variables/01-hello` with a wrong solution and confirm the FAIL diff renders. Fix it and confirm PASS renders with a timing under 300 ms on a warm cache.

### Step 5 — Progress
Implement `runner/src/progress.rs` with atomic writes and corruption recovery.

**Acceptance:** `cargo progress` prints a dashboard for the one existing exercise. A truncated `progress.json` is backed up and recreated rather than crashing the runner. Compile errors increment `compileErrors`, not `attempts`.

### Step 6 — Watcher
Implement `runner/src/bin/watch.rs` including debouncing, run serialisation, `strict_progression`, the level-16 non-bin rule, and the level-complete celebration.

**Acceptance:** `cargo dev` runs; saving an exercise grades it in under 300 ms; saving a level-03 exercise while level 02 is incomplete prints the progression message instead of grading; rapid repeated saves never interleave two runs.

### Step 7 — CLI
Implement `runner/src/bin/cli.rs` and wire up `grade`, `grade-level`, `progress`, `solution` (with the 3-failure lock), `reset`, and `reset-checks`.

**Acceptance:** each command works and prints a helpful message on bad input. `solution` refuses before 3 *non-compile* failures. All aliases in `.cargo/config.toml` resolve.

### Step 8 — Test grading
Implement the `cargo test --no-run` path from §5.5, the libtest output parser, the per-check result display, and the `checks.lock` tamper check from §5.6.

**Acceptance:** `08-functions/01-add` fails with a readable per-check breakdown when `add` is wrong, passes when right, and refuses to grade after `checks/01-add.rs` is edited until `cargo reset-checks` is run.

### Step 9 — Content generation
Generate all 16 level crates. For each exercise in §9: the stub file (per §4's format), the reference solution in `solutions/`, the `checks/<name>.rs` where marked **[T]**, and a `hints.toml` entry where a hint helps. Then write and run `cargo gen-expected`.

Do this **one level at a time**, verifying each level fully before moving to the next. Do not generate all 200 in one pass.

**Acceptance per level:** `cargo verify --level NN` shows 100% pass against the solutions. Every stub compiles when the learner's section is empty (that's what `todo!()` is for in test-graded stubs). No stub contains a solution. No level crate has dependencies.

### Step 10 — Level READMEs
Write a `README.md` per level using the §8 template. Verify every code snippet actually compiles and produces the output shown in its comments — write `cargo verify-readmes` that extracts fenced `rust` blocks, wraps bare statements in a `fn main`, and compiles them. Levels 09 onward must list their `error[EXXXX]` codes.

**Acceptance:** a reader who knows only levels 1..N-1 can understand level N's README with no external lookup. Every snippet compiles.

### Step 11 — Root README
Write `README.md` for a complete beginner: how to install Rust with `rustup`, how to clone, `cargo dev`, what PASS, FAIL and DOESN'T COMPILE look like (with output-as-text examples), what to do when stuck, and the rules from the learning plan. Assume she has never used a terminal. Include the exact commands to copy. Include a short "how to read a Rust error message" section with an annotated `E0382` — it is the single highest-value page in the repo.

**Acceptance:** someone who has never installed Rust could follow it start to finish.

### Step 12 — Full pass (Phase 1)
Run `cargo verify --level` for each of levels 01–16 — must be **200/200**. Reset progress. Verify `cargo dev` from a clean state starts at level 01. Time a cold-cache first run and a warm-cache edit; record both in the root README.

When Phases 3–6 are present, the **repo-wide** gate is **456/456** (`cargo verify` with no filter). Phase 1 exercise crates stay dependency-free; later phases use workspace crates per the phases 3–6 spec and may use longer per-level timeouts.

---

## 11. Quality bar

These are the things that will make or break whether she actually uses this. Treat them as requirements, not polish.

1. **Feedback in under 300 ms on a warm cache.** §7 is how. If the runner feels slow she'll stop trusting it.
2. **Compile errors are the main verdict, so they get the best treatment.** Pass rustc's rendered output through untouched, cap at 3 errors, strip macro-origin noise, and never let a compile error count against her attempt budget.
3. **Failure messages never blame.** `Not quite — your line 4 prints 3, expected 2.` Not `ERROR: assertion failed`. And never `✗ FAILED` alone for a compile error — it says `DOESN'T COMPILE`, which is a different and much less discouraging thing.
4. **No backtraces, ever.** A beginner seeing 30 frames of internal Rust will panic. Show the error type, the message, and the line in *her* file. Nothing else. This is why `debug = 0` costs us nothing.
5. **No jargon in anything she reads.** Stubs, READMEs, and runner output use words she's already met. "Function" is fine at level 08. "Borrow" needs a sentence of explanation the first time, at level 09. "Lifetime" does not appear anywhere in Phase 1 except as a named error code she might encounter.
6. **Every level ends with a visible win.** The level-complete block should genuinely feel like something.
7. **The repo runs on a fresh machine** with only `rustup` installed. No global installs, no editor plugins required, no network access needed after the first `cargo build` (exercise crates have no dependencies to fetch).
