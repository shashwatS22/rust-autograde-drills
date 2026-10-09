//! 27-threads / 08-atomic-two-threads
//!
//! TASK
//! Increment an `AtomicUsize` from two threads.
//!
//! SIGNATURE
//! fn two_thread_inc() -> usize
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::sync::atomic::{AtomicUsize, Ordering};
use std::sync::Arc;
use std::thread;
fn two_thread_inc() -> usize {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-atomic-two-threads.rs"]
mod tests;