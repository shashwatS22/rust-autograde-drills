//! 38-sync-primitives / 01-atomic-fetch-two
//!
//! TASK
//! Two threads `fetch_add` into one `AtomicUsize`.
//!
//! CONCEPT
//! AtomicUsize fetch_add is lock-free addition safe to share across threads.
//!
//! SIGNATURE
//! fn parallel_add() -> usize
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::sync::atomic::{AtomicUsize, Ordering};
use std::sync::Arc;
use std::thread;
fn parallel_add() -> usize {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-atomic-fetch-two.rs"]
mod tests;