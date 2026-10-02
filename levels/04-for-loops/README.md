# Level 04 — For loops

## What you'll learn
- `1..=10` inclusive ranges
- `.rev()`
- `.step_by()`
- accumulators

## Concepts

```rust
fn main() {
    for i in 1..=3 {
        println!("{i}");
    }
}
// 1
// 2
// 3
```

## Common mistakes
- Off-by-one: `1..10` stops at 9; use `1..=10` for 10 inclusive.

## Before you start
Type every example above into `playground/src/main.rs` and run it with
`cargo play`. Change a number and predict what happens before you run it again.

## Exercises
Work through the exercises in order. Save each file to check it.
