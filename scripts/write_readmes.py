#!/usr/bin/env python3
"""Generate level README.md files from templates."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVELS = ROOT / "levels"

READMES = {
    "01-print-and-variables": (
        "Print & variables",
        ["`println!`", "`let` and `let mut`", "shadowing", "formatting with `{:.2}`"],
        """```rust
fn main() {
    let name = "Riya";
    println!("Hello, {name}!");
}
// Hello, Riya!
```""",
        ["Forgetting quotes around text — use `\"Hello\"` inside `println!`."],
    ),
    "02-operators": (
        "Operators",
        ["arithmetic on integers", "`as` casting", "`checked_add` / `wrapping_add`", "precedence"],
        """```rust
fn main() {
    let a: i32 = 17;
    let b: i32 = 5;
    println!("{}", a / b);
}
// 3
```""",
        ["`17 / 5` is `3`, not `3.4` — integer division truncates."],
    ),
    "03-conditionals-and-match": (
        "Conditionals & match",
        ["`if` / `else`", "`if` as an expression", "`match` with ranges"],
        """```rust
fn main() {
    let n = 10;
    let label = if n % 2 == 0 { "even" } else { "odd" };
    println!("{label}");
}
// even
```""",
        ["Rust has no ternary operator — the `if` expression returns a value."],
    ),
    "04-for-loops": (
        "For loops",
        ["`1..=10` inclusive ranges", "`.rev()`", "`.step_by()`", "accumulators"],
        """```rust
fn main() {
    for i in 1..=3 {
        println!("{i}");
    }
}
// 1
// 2
// 3
```""",
        ["Off-by-one: `1..10` stops at 9; use `1..=10` for 10 inclusive."],
    ),
    "05-while-and-loop": (
        "While & loop",
        ["`while`", "`loop` with `break` value", "labelled `break`"],
        """```rust
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
```""",
        ["Infinite loops: make sure something inside the loop moves toward the exit."],
    ),
    "06-patterns": (
        "Nested loops & patterns",
        ["building a row as a `String`", "one `println!` per row"],
        """```rust
fn main() {
    let mut row = String::new();
    row.push_str("*");
    row.push_str("*");
    println!("{row}");
}
// **
```""",
        ["Using many `print!` calls — build one line, then print it once."],
    ),
    "07-number-problems": (
        "Number problems",
        ["digit extraction with `%` and `/`", "primes and divisors", "GCD / LCM"],
        """```rust
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
```""",
        ["Testing divisibility: loop while `i * i <= n`, not only while `i <= n`."],
    ),
    "08-functions": (
        "Functions",
        ["`fn` and return types", "closures", "`impl Fn`"],
        """```rust
fn add(a: i32, b: i32) -> i32 {
    a + b
}
fn main() {
    println!("{}", add(2, 3));
}
// 5
```""",
        ["Semicolon on the last line turns the return into `()`."],
    ),
    "09-ownership-and-borrowing": (
        "Ownership & borrowing",
        ["move vs `Copy`", "`&` and `&mut`", "slices"],
        """```rust
fn main() {
    let s1 = String::from("hello");
    let s2 = s1;
    println!("{s2}");
}
// hello
```""",
        [
            "**E0382** — use after move.",
            "**E0499** — two mutable borrows at once.",
            "**E0502** — mutable and immutable borrow overlap.",
        ],
    ),
    "10-strings": (
        "Strings",
        ["`String` vs `&str`", "`.chars()`", "byte vs char indexing"],
        """```rust
fn main() {
    let s = "rust";
    for c in s.chars() {
        println!("{c}");
    }
}
// r
// u
// s
// t
```""",
        ["Indexing a `String` with `[0]` — use `.chars()` or `.as_bytes()`."],
    ),
    "11-vectors-and-slices": (
        "Vectors & slices",
        ["`vec![]`", "`&[T]` parameters", "in-place algorithms"],
        """```rust
fn main() {
    let v = vec![1, 2, 3];
    println!("{}", v[0]);
}
// 1
```""",
        ["Borrowing: use `for x in &v` if you still need `v` after the loop."],
    ),
    "12-iterators-and-closures": (
        "Iterators & closures",
        ["`.iter()`", "`.map` / `.filter` / `.fold`", "method chaining"],
        """```rust
fn main() {
    let v = vec![1, 2, 3];
    let sum: i32 = v.iter().sum();
    println!("{sum}");
}
// 6
```""",
        ["`.sort()` on `[10, 9, 100]` needs `sort_by` for numeric order."],
    ),
    "13-structs-and-enums": (
        "Structs & enums",
        ["`struct` and `impl`", "`enum` with data", "`Option` / `Result`"],
        """```rust
struct Point { x: i32, y: i32 }
fn main() {
    let p = Point { x: 1, y: 2 };
    println!("{}", p.x);
}
// 1
```""",
        ["Forgetting `mut` on a binding when changing a struct field."],
    ),
    "14-recursion": (
        "Recursion",
        ["base case", "recursive case", "call stack"],
        """```rust
fn fact(n: u64) -> u64 {
    if n <= 1 { 1 } else { n * fact(n - 1) }
}
fn main() {
    println!("{}", fact(5));
}
// 120
```""",
        ["Missing base case → stack overflow on large input."],
    ),
    "15-hashmaps-and-sets": (
        "HashMaps & sets",
        ["`HashMap`", "`BTreeMap` for sorted keys", "frequency counting"],
        """```rust
use std::collections::HashMap;
fn main() {
    let mut m = HashMap::new();
    *m.entry('a').or_insert(0) += 1;
    println!("{:?}", m.get(&'a'));
}
// Some(1)
```""",
        ["HashMap iteration order is random — sort keys when printing."],
    ),
    "16-modules-errors-io": (
        "Modules, errors & I/O",
        ["`mod` / `use`", "`Result` and `?`", "reading files"],
        """```rust
fn main() -> Result<(), Box<dyn std::error::Error>> {
    let text = std::fs::read_to_string("data/sample.txt")?;
    println!("{}", text.trim());
    Ok(())
}
// hello from a file
```""",
        ["Run exercises from the level crate directory — paths like `data/sample.txt` are relative to it."],
    ),
}


def write_readme(level_dir: str, num: int, title: str, bullets, example, mistakes):
    learn = "\n".join(f"- {b}" for b in bullets)
    mistakes_md = "\n".join(f"- {m}" for m in mistakes)
    body = f"""# Level {num:02} — {title}

## What you'll learn
{learn}

## Concepts

{example}

## Common mistakes
{mistakes_md}

## Before you start
Type every example above into `playground/src/main.rs` and run it with
`cargo play`. Change a number and predict what happens before you run it again.

## Exercises
Work through the exercises in order. Save each file to check it.
"""
    path = LEVELS / level_dir / "README.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body)


def main():
    for level_dir in sorted(LEVELS.iterdir()):
        if not level_dir.is_dir():
            continue
        key = level_dir.name
        if key not in READMES:
            continue
        title, bullets, example, mistakes = READMES[key]
        num = int(key.split("-")[0])
        write_readme(key, num, title, bullets, example, mistakes)
    print("Wrote README.md for", len(READMES), "levels")


if __name__ == "__main__":
    main()
