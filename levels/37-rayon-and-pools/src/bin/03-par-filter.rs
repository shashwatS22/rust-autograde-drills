//! 37-rayon-and-pools / 03-par-filter
//!
//! TASK
//! Collect even numbers using `filter` on a parallel range.
//!
//! SIGNATURE
//! fn evens() -> Vec<i32>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use rayon::prelude::*;
fn evens() -> Vec<i32> {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/03-par-filter.rs"]
mod tests;