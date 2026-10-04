# Level 40 — Unsafe Rust

## What you'll learn
- raw pointers
- invariants
- sound abstractions

## Concepts

Every `unsafe` block must uphold an invariant stated in your comment.

```rust
fn main() {
    println!("Type examples from this README into playground with `cargo play`.");
}
```

## Common mistakes
- Calling `unsafe` to silence the borrow checker without documenting why it's sound.

## Before you start
Run `cargo warm 40` if this level uses external crates (see `level.toml`). Type examples into `playground` with `cargo play`.

## Exercises
Work through the exercises in order. Save each file to check it.
