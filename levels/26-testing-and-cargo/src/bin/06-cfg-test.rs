//! 26-testing-and-cargo / 06-cfg-test
//!
//! TASK
//! Implement `cfg test` as described in the stub.
//!
//! SIGNATURE
//! pub fn prod() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
pub fn prod() -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/06-cfg-test.rs"]
mod tests;
