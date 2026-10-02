# Level 14 — Recursion

## What you'll learn
- base case
- recursive case
- call stack

## Concepts

```rust
fn fact(n: u64) -> u64 {
    if n <= 1 { 1 } else { n * fact(n - 1) }
}
fn main() {
    println!("{}", fact(5));
}
// 120
```

## Common mistakes
- Missing base case → stack overflow on large input.

## Before you start
Type every example above into `playground/src/main.rs` and run it with
`cargo play`. Change a number and predict what happens before you run it again.

## Exercises
Work through the exercises in order. Save each file to check it.
