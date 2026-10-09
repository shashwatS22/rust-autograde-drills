//! 38-sync-primitives / 05-ordering-relaxed
//!
//! TASK
//! Increment with `Ordering::Relaxed`.
//!
//! SIGNATURE
//! fn relaxed_inc() -> usize
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::sync::atomic::{AtomicUsize, Ordering};
fn relaxed_inc() -> usize {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/05-ordering-relaxed.rs"]
mod tests;