# rust-bootcamp

Auto-graded Rust drills: open an exercise, write code, save — the terminal shows **PASS**, **FAIL**, or **DOESN'T COMPILE** immediately.

## Install Rust (first time only)

1. Open a terminal.
2. Run:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

3. Follow the prompts (defaults are fine).
4. Restart the terminal, then check:

```bash
rustc --version
cargo --version
```

You want Rust **1.90** or newer (this repo pins it via `rust-toolchain.toml`).

## Get started

```bash
cd rust-bootcamp   # this folder
cargo dev
```

Leave that running. Open any file under `levels/<level>/src/bin/`, write your code, and **save**. The watcher grades that file automatically.

Other commands:

| Command | What it does |
|---|---|
| `cargo play` | Run `playground/src/main.rs` (experiments, never graded) |
| `cargo grade <id>` | Grade one exercise once, e.g. `cargo grade 04-for-loops/07-count-digits` |
| `cargo grade-level 04` | Grade every exercise in level 04 |
| `cargo progress` | Dashboard of what’s done |
| `cargo solution <id>` | Show reference solution (locked until 3 failed runs; compile errors don’t count) |

Write notes in `NOTES.md`. Read each level’s `README.md` before its exercises.

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

On a typical dev machine with a warm cache, one exercise rebuild + run is about **200–300 ms** after the first build. The first build of a level takes longer while Cargo compiles that crate.

## Roadmap

See [reference/LEARNING-PLAN.md](reference/LEARNING-PLAN.md) for the full learning path (200 drills + LeetCode + later backend/systems/WASM tracks).
