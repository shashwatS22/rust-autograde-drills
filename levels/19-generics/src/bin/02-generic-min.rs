//! 19-generics / 02-generic-min
//!
//! TASK
//! Implement `generic min` as described in the stub.
//!
//! CONCEPT
//! Generic functions reuse logic for many types; the bound lists what operations T must support.
//!
//! SIGNATURE
//! fn min_i32(a: i32, b: i32) -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn min_i32(a: i32, b: i32) -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/02-generic-min.rs"]
mod tests;