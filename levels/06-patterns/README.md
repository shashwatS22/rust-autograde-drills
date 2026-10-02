# Level 06 — Nested loops & patterns

## What you'll learn
- building a row as a `String`
- one `println!` per row

## Concepts

```rust
fn main() {
    let mut row = String::new();
    row.push_str("*");
    row.push_str("*");
    println!("{row}");
}
// **
```

## Common mistakes
- Using many `print!` calls — build one line, then print it once.

## Before you start
Type every example above into `playground/src/main.rs` and run it with
`cargo play`. Change a number and predict what happens before you run it again.

## Exercises
Work through the exercises in order. Save each file to check it.
