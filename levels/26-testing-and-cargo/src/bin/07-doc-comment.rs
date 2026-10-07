//! 26-testing-and-cargo / 07-doc-comment
//!
//! TASK
//! Document a public API with `///` (rustdoc reads it).
//!
//! SIGNATURE
//! pub fn triple(x: i32) -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
/// Returns three times `x`.
pub fn triple(x: i32) -> i32 { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/07-doc-comment.rs"]
mod tests;
