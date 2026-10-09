//! 18-derive-and-operators / 02-derive-clone
//!
//! TASK
//! Implement `derive clone` as described in the stub.
//!
//! CONCEPT
//! Derive Clone to get .clone() for types whose fields are all Clone.
//!
//! SIGNATURE
//! fn cloned() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn cloned() -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/02-derive-clone.rs"]
mod tests;