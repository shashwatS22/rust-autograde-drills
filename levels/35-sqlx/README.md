# Level 35 — SQLx

## What you'll learn
- SQLite in memory
- runtime queries
- migrations in drills

## Concepts

Drills use `sqlite::memory:` only. Postgres is for `projects/api`.

```rust
fn main() {
    println!("Type examples from this README into playground with `cargo play`.");
}
```

## Common mistakes
- Using `query!` without offline data — prefer runtime API in drills.

## Before you start
Run `cargo warm 35` if this level uses external crates (see `level.toml`). Type examples into `playground` with `cargo play`.

## Exercises
Work through the exercises in order. Save each file to check it.
