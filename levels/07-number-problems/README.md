# Level 07 — Number problems

## What you'll learn
- digit extraction with `%` and `/`
- primes and divisors
- GCD / LCM

## Concepts

```rust
fn main() {
    let n: u32 = 74821;
    let mut c = 0;
    let mut x = n;
    while x > 0 {
        c += 1;
        x /= 10;
    }
    println!("{c}");
}
// 5
```

## Common mistakes
- Testing divisibility: loop while `i * i <= n`, not only while `i <= n`.

## Before you start
Type every example above into `playground/src/main.rs` and run it with
`cargo play`. Change a number and predict what happens before you run it again.

## Exercises
Work through the exercises in order. Save each file to check it.
