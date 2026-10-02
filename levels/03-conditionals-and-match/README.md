# Level 03 — Conditionals & match

## What you'll learn
- `if` / `else`
- `if` as an expression
- `match` with ranges

## Concepts

```rust
fn main() {
    let n = 10;
    let label = if n % 2 == 0 { "even" } else { "odd" };
    println!("{label}");
}
// even
```

## Common mistakes
- Rust has no ternary operator — the `if` expression returns a value.

## Before you start
Type every example above into `playground/src/main.rs` and run it with
`cargo play`. Change a number and predict what happens before you run it again.

## Exercises
Work through the exercises in order. Save each file to check it.
