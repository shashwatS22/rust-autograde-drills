# Level 13 — Structs & enums

## What you'll learn
- `struct` and `impl`
- `enum` with data
- `Option` / `Result`

## Concepts

```rust
struct Point { x: i32, y: i32 }
fn main() {
    let p = Point { x: 1, y: 2 };
    println!("{}", p.x);
}
// 1
```

## Common mistakes
- Forgetting `mut` on a binding when changing a struct field.

## Before you start
Type every example above into `playground/src/main.rs` and run it with
`cargo play`. Change a number and predict what happens before you run it again.

## Exercises
Work through the exercises in order. Save each file to check it.
