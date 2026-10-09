//! 18-derive-and-operators / 05-add-assign
//!
//! TASK
//! Implement `add assign` as described in the stub.
//!
//! CONCEPT
//! The AddAssign trait (or derive) enables += on your type when the stub implements operator traits.
//!
//! SIGNATURE
//! fn bump() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::ops::AddAssign;
fn bump() -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/05-add-assign.rs"]
mod tests;