//! 26-testing-and-cargo / 08-test-helper
//!
//! TASK
//! Combine assertions in one graded test.
//!
//! SIGNATURE
//! pub fn greet(name: &str) -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
pub fn greet(name: &str) -> String { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-test-helper.rs"]
mod tests;
