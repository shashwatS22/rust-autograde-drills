# Level 11 — Vectors & slices

## What you'll learn
- `vec![]`
- `&[T]` parameters
- in-place algorithms

## Concepts

```rust
fn main() {
    let v = vec![1, 2, 3];
    println!("{}", v[0]);
}
// 1
```

## Common mistakes
- Borrowing: use `for x in &v` if you still need `v` after the loop.

## Before you start
Type every example above into `playground/src/main.rs` and run it with
`cargo play`. Change a number and predict what happens before you run it again.

## Exercises
Work through the exercises in order. Save each file to check it.
