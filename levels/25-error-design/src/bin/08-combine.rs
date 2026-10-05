//! 25-error-design / 08-combine
//!
//! TASK
//! Implement `combine` as described in the stub.
//!
//! SIGNATURE
//! fn both(a: Result<i32, ()>, b: Result<i32, ()>) -> Result<i32, ()>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn both(a: Result<i32, ()>, b: Result<i32, ()>) -> Result<i32, ()> {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-combine.rs"]
mod tests;
