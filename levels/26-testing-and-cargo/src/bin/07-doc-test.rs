//! 26-testing-and-cargo / 07-doc-test
//!
//! TASK
//! Implement `doc test` as described in the stub.
//!
//! SIGNATURE
//! pub fn plus(a: i32, b: i32) -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
pub fn plus(a: i32, b: i32) -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/07-doc-test.rs"]
mod tests;
