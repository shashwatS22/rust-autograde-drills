//! 28-channels-and-sync / 04-barrier
//!
//! TASK
//! Implement `barrier` as described in the stub.
//!
//! SIGNATURE
//! fn wait() -> usize
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::sync::{Arc, Barrier};
use std::thread;
fn wait() -> usize {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/04-barrier.rs"]
mod tests;
