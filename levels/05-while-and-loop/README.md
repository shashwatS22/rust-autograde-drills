# Level 05 — While & loop

## What you'll learn
- `while`
- `loop` with `break` value
- labelled `break`

## Concepts

```rust
fn main() {
    let mut n = 3;
    while n > 0 {
        println!("{n}");
        n -= 1;
    }
}
// 3
// 2
// 1
```

## Common mistakes
- Infinite loops: make sure something inside the loop moves toward the exit.

## Before you start
Type every example above into `playground/src/main.rs` and run it with
`cargo play`. Change a number and predict what happens before you run it again.

## Exercises
Work through the exercises in order. Save each file to check it.
