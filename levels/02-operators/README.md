# Level 02 — Operators

## What you'll learn
- arithmetic on integers
- `as` casting
- `checked_add` / `wrapping_add`
- precedence

## Concepts

```rust
fn main() {
    let a: i32 = 17;
    let b: i32 = 5;
    println!("{}", a / b);
}
// 3
```

## Common mistakes
- `17 / 5` is `3`, not `3.4` — integer division truncates.

## Before you start
Type every example above into `playground/src/main.rs` and run it with
`cargo play`. Change a number and predict what happens before you run it again.

## Exercises
Work through the exercises in order. Save each file to check it.
