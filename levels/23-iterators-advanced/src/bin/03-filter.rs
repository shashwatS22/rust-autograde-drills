//! 23-iterators-advanced / 03-filter
//!
//! TASK
//! Implement `filter` as described in the stub.
//!
//! CONCEPT
//! filter keeps elements where the closure returns true; lazy until collect or for_each.
//!
//! SIGNATURE
//! fn evens(v: &[i32]) -> Vec<i32>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn evens(v: &[i32]) -> Vec<i32> {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/03-filter.rs"]
mod tests;