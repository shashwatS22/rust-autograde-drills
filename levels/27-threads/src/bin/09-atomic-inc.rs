//! 27-threads / 09-atomic-inc
//!
//! TASK
//! Complete `09-atomic-inc` (atomic inc).
//!
//! SIGNATURE
//! fn inc() -> usize
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::sync::atomic::{AtomicUsize, Ordering};
fn inc() -> usize {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/09-atomic-inc.rs"]
mod tests;
