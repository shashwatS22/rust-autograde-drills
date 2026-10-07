//! 26-testing-and-cargo / 06-result-ok
//!
//! TASK
//! Return `Result` and test with `is_ok` / `unwrap`.
//!
//! SIGNATURE
//! pub fn parse_one(s: &str) -> Result<i32, ()>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
pub fn parse_one(s: &str) -> Result<i32, ()> { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/06-result-ok.rs"]
mod tests;
