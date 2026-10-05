//! 28-channels-and-sync / 03-condvar
//!
//! TASK
//! Implement `condvar` as described in the stub.
//!
//! SIGNATURE
//! fn signal() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::sync::{Arc, Mutex, Condvar};
fn signal() -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/03-condvar.rs"]
mod tests;
