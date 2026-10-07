//! 38-sync-primitives / 08-barrier-two
//!
//! TASK
//! Synchronize two threads with `Barrier`.
//!
//! SIGNATURE
//! fn both_ready() -> usize
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::sync::{Arc, Barrier};
use std::thread;
fn both_ready() -> usize {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-barrier-two.rs"]
mod tests;
