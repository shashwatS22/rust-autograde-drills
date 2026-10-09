//! 23-iterators-advanced / 08-collect-result
//!
//! TASK
//! Use `collect` to build a `Result<Vec<_>, _>`.
//!
//! SIGNATURE
//! fn parse_all(v: &[&str]) -> Result<Vec<i32>, std::num::ParseIntError>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn parse_all(v: &[&str]) -> Result<Vec<i32>, std::num::ParseIntError> {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-collect-result.rs"]
mod tests;