//! 25-error-design / 07-question
//!
//! TASK
//! Implement `question` as described in the stub.
//!
//! CONCEPT
//! The ? operator propagates Err; the function signature must use a compatible error type.
//!
//! SIGNATURE
//! fn div(a: i32, b: i32) -> Result<i32, &'static str>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn div(a: i32, b: i32) -> Result<i32, &'static str> {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/07-question.rs"]
mod tests;