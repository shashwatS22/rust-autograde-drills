# Level 16 — Modules, errors & I/O

## What you'll learn
- `mod` / `use`
- `Result` and `?`
- reading files

## Concepts

```rust
fn main() -> Result<(), Box<dyn std::error::Error>> {
    let text = std::fs::read_to_string("data/sample.txt")?;
    println!("{}", text.trim());
    Ok(())
}
// hello from a file
```

## Common mistakes
- Run exercises from the level crate directory — paths like `data/sample.txt` are relative to it.

## Before you start
Type every example above into `playground/src/main.rs` and run it with
`cargo play`. Change a number and predict what happens before you run it again.

## Exercises
Work through the exercises in order. Save each file to check it.
