# Level 09 — Ownership & borrowing

## What you'll learn
- move vs `Copy`
- `&` and `&mut`
- slices

## Concepts

```rust
fn main() {
    let s1 = String::from("hello");
    let s2 = s1;
    println!("{s2}");
}
// hello
```

## Common mistakes
- **E0382** — use after move.
- **E0499** — two mutable borrows at once.
- **E0502** — mutable and immutable borrow overlap.

## Before you start
Type every example above into `playground/src/main.rs` and run it with
`cargo play`. Change a number and predict what happens before you run it again.

## Exercises
Work through the exercises in order. Save each file to check it.
