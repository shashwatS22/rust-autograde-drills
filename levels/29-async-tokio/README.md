# Level 29 — Async & Tokio

## What you'll learn
- `async fn` and `.await`
- Tokio runtime
- deterministic tests with `pause()`

## Concepts

Run `cargo warm 29` first. Checks use `tokio::time::pause()` — no real sleeping.

```rust
fn main() {
    println!("Type examples from this README into playground with `cargo play`.");
}
```

## Common mistakes
- Blocking the executor with `std::thread::sleep` inside async code.

## Before you start
Run `cargo warm 29` if this level uses external crates (see `level.toml`). Type examples into `playground` with `cargo play`.

## Exercises
Work through the exercises in order. Save each file to check it.
