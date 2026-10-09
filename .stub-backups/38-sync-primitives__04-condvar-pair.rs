//! 38-sync-primitives / 04-condvar-pair
//!
//! TASK
//! Wait on a `Condvar` until another thread updates data.
//!
//! SIGNATURE
//! fn worker_wakes() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::sync::{Arc, Condvar, Mutex};
use std::thread;
fn worker_wakes() -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/04-condvar-pair.rs"]
mod tests;