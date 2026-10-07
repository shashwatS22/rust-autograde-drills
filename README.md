# rust-autograde-drills

**456 auto-graded Rust exercises** from fundamentals through backend and browser stacks: **Axum**, **Tokio**, **Serde**, **SQLx**, **Tower/tracing**, auth (argon2/JWT), **Rayon**, **unsafe/FFI**, **Leptos**, and **wasm-bindgen** — plus capstone projects under `projects/`.

Open a drill under `levels/`, write code, **save**; the watcher shows **PASS**, **FAIL**, or **DOESN'T COMPILE** immediately (stdout diff or compiler output).

**Author:** [Shashwat Sharma](https://github.com/shashwatS22) · **License:** [MIT](LICENSE)

## Clone & run

```bash
git clone https://github.com/shashwatS22/rust-autograde-drills.git
cd rust-autograde-drills
cargo dev
```

Leave `cargo dev` running. Open any file under `levels/<level>/src/bin/`, implement the task, and **save**. The watcher grades that file automatically.

### Requirements

- Rust **1.90+** ([rustup](https://rustup.rs/)); this repo pins the toolchain via `rust-toolchain.toml`.

## Commands

| Command | What it does |
|---|---|
| `cargo dev` | File watcher — grade on save (main learning loop) |
| `cargo play` | Run `playground/src/main.rs` (experiments, never graded) |
| `cargo grade <id>` | Grade one exercise once, e.g. `cargo grade 04-for-loops/07-count-digits` |
| `cargo grade-level 04` | Grade every exercise in level 04 |
| `cargo progress` | Dashboard by phase and by level |
| `cargo warm <NN>` | Pre-build level NN (run once before levels with dependencies) |
| `cargo solution <id>` | Reference solution (locked until 3 failed runs; compile errors don’t count) |
| `cargo reset <id>` | Restore stub and clear progress for one exercise (`yes` to confirm) |
| `cargo reset <NN>` | Reset an entire level |
| `cargo verify` | Grade all **456** solution binaries (maintainer / CI check) |

Write personal notes in `NOTES.md` (gitignored). Read each level’s `README.md` before its exercises.

## What PASS looks like

```
✓ PASS  01-print-and-variables/01-hello (231ms)
        Level 01 — 1/12 done
```

## What FAIL looks like

```
✗ FAIL  04-for-loops/12-fibonacci

  line  expected          your output
  ────  ────────────────  ────────────────
   4    2                 3      ← first difference
```

## What DOESN'T COMPILE looks like (normal)

Most saves in Rust fail to compile first. That is expected.

```
✗ DOESN'T COMPILE  09-ownership-and-borrowing/01-move

error[E0382]: borrow of moved value: `s1`
 --> src/bin/01-move.rs:4:16
  |
3 |     let s2 = s1;
  |              -- value moved here
4 |     println!("{s1}");
  |                ^^ value borrowed here after move
```

### How to read a Rust error (E0382)

1. **`error[E0382]`** — look this up with `rustc --explain E0382`.
2. **Message** — plain English: you used a value after it was moved.
3. **Arrows** — `-- value moved here` and `^^ value borrowed here` point at the exact lines.
4. **`help:`** — often suggests a fix (e.g. `.clone()`). Understand *why* before applying it.

Read the message top to bottom once, out loud if it helps, then change one thing and save again.

## When you’re stuck

1. Re-read the level `README.md`.
2. After **15 minutes**, read it again.
3. After **25 minutes**, `cargo solution <id>`, read, close, delete your attempt, rewrite from memory.

**Rules:** type exercises by hand (no paste). Don’t skip a level until it’s all green. No `.clone()` to silence the borrow checker without a note in `NOTES.md`.

## Performance (reference machine)

- **Levels 01–16** (no dependencies): ~**200–300 ms** save → verdict on a warm cache.
- **Levels 17–48** (with crates): run **`cargo warm NN`** once per level (~30–90 s first time), then ~**300–600 ms** per save.

Capstone projects (`projects/api`, `projects/systems`, `projects/web`) use `cargo test -p …`, not the exercise watcher.

## Curriculum map

| Phases | Levels | Drills | Topics (high level) |
|--------|--------|--------|---------------------|
| 1 | 01–16 | 200 | Syntax, ownership, collections, modules |
| 3 | 17–29 | 104 | Traits, async, threads, errors |
| 4 | 30–36 | 56 | Serde, Axum, Tower, SQLx, auth |
| 5 | 37–43 | 56 | Rayon, layout, unsafe, FFI, CLI |
| 6 | 44–48 | 40 | wasm-bindgen, Leptos, DOM-shaped drills |

Full maintainer specs: [reference/BUILD-SPEC.md](reference/BUILD-SPEC.md) (Phase 1), [reference/BUILD-SPEC-PHASES-3-6.md](reference/BUILD-SPEC-PHASES-3-6.md) (Phases 3–6). Learner roadmap: [reference/LEARNING-PLAN.md](reference/LEARNING-PLAN.md).

Track B DSA: LeetCode + [`cargo dsa`](dsa/sections.toml). Library capstones: `projects/matrix`, `projects/kvstore`. Web fundamentals: `projects/web-fundamentals/`.
