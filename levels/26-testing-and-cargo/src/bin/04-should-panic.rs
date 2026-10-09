//! 26-testing-and-cargo / 04-should-panic
//!
//! TASK
//! Function that panics on invalid input; check uses `catch_unwind`.
//!
//! SIGNATURE
//! pub fn divide(a: i32, b: i32) -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
pub fn divide(a: i32, b: i32) -> i32 { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/04-should-panic.rs"]
mod tests;