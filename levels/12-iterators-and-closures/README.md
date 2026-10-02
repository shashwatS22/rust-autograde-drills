# Level 12 — Iterators & closures

## What you'll learn
- `.iter()`
- `.map` / `.filter` / `.fold`
- method chaining

## Concepts

```rust
fn main() {
    let v = vec![1, 2, 3];
    let sum: i32 = v.iter().sum();
    println!("{sum}");
}
// 6
```

## Common mistakes
- `.sort()` on `[10, 9, 100]` needs `sort_by` for numeric order.

## Before you start
Type every example above into `playground/src/main.rs` and run it with
`cargo play`. Change a number and predict what happens before you run it again.

## Exercises
Work through the exercises in order. Save each file to check it.
