# Level 15 — HashMaps & sets

## What you'll learn
- `HashMap`
- `BTreeMap` for sorted keys
- frequency counting

## Concepts

```rust
use std::collections::HashMap;
fn main() {
    let mut m = HashMap::new();
    *m.entry('a').or_insert(0) += 1;
    println!("{:?}", m.get(&'a'));
}
// Some(1)
```

## Common mistakes
- HashMap iteration order is random — sort keys when printing.

## Before you start
Type every example above into `playground/src/main.rs` and run it with
`cargo play`. Change a number and predict what happens before you run it again.

## Exercises
Work through the exercises in order. Save each file to check it.
