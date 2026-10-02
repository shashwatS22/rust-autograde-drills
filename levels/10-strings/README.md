# Level 10 — Strings

## What you'll learn
- `String` vs `&str`
- `.chars()`
- byte vs char indexing

## Concepts

```rust
fn main() {
    let s = "rust";
    for c in s.chars() {
        println!("{c}");
    }
}
// r
// u
// s
// t
```

## Common mistakes
- Indexing a `String` with `[0]` — use `.chars()` or `.as_bytes()`.

## Before you start
Type every example above into `playground/src/main.rs` and run it with
`cargo play`. Change a number and predict what happens before you run it again.

## Exercises
Work through the exercises in order. Save each file to check it.
