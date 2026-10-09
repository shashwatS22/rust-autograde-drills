//! 22-conversions / 03-try-from
//!
//! TASK
//! Implement `try from` as described in the stub.
//!
//! CONCEPT
//! TryFrom returns Result when conversion can fail, unlike infallible From.
//!
//! SIGNATURE
//! fn parse() -> Result<i32, std::num::TryFromIntError>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn parse() -> Result<i32, std::num::TryFromIntError> {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/03-try-from.rs"]
mod tests;