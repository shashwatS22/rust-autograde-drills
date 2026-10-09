//! 02-operators / 10-math-methods
//!
//! TASK
//! Print `(-7i32).abs()`, `2i32.pow(10)`, `144f64.sqrt()`, `4.6f64.round()`, `3.max(9).max(2)`.
//!
//! EXPECTED OUTPUT
//! `7
//! 1024
//! 12
//! 5
//! 9`

fn main() {
    // Your code below
        println!("{}", (-7i32).abs());
    println!("{}", 2i32.pow(10));
    println!("{}", 144f64.sqrt());
    println!("{}", 4.6f64.round());
    println!("{}", 3.max(9).max(2));
}