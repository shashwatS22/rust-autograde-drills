//! 02-operators / 09-parse-failure
//!
//! TASK
//! GIVEN `s = "abc"`. Print `s.parse::<i32>().is_err()`, then `s.parse::<i32>().unwrap_or(0)`.
//!
//! CONCEPT
//! When parse fails it returns Result. is_err() is true for bad input; unwrap_or(0) uses 0 instead of panicking.
//!
//! EXPECTED OUTPUT
//! `true
//! 0`

fn main() {
    // ---- GIVEN ----
    let s = "abc";
    // ---------------

    // Your code below
    println!("{}", s.parse::<i32>().is_err());
    println!("{}", s.parse::<i32>().unwrap_or(0));
}