//! 02-operators / 02-float-divide
//!
//! TASK
//! GIVEN `a: f64 = 17.0`, `b: f64 = 5.0`. Print `a / b`.
//!
//! CONCEPT
//! f64 values use floating-point division, so 17.0 / 5.0 keeps the decimal part.
//!
//! EXPECTED OUTPUT
//! `3.4`

use std::print;

fn main() {
    // ---- GIVEN ----
    let a: f64 = 17.0;
    let b: f64 = 5.0;
    // ---------------

    // Your code below
    print!("{}", a / b)
}