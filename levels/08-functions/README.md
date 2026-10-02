# Level 08 — Functions

## What you'll learn
- `fn` and return types
- closures
- `impl Fn`

## Concepts

```rust
fn add(a: i32, b: i32) -> i32 {
    a + b
}
fn main() {
    println!("{}", add(2, 3));
}
// 5
```

## Common mistakes
- Semicolon on the last line turns the return into `()`.

## Before you start
Type every example above into `playground/src/main.rs` and run it with
`cargo play`. Change a number and predict what happens before you run it again.

## Exercises
Work through the exercises in order. Save each file to check it.
