//! 28-channels-and-sync / 05-rwlock
//!
//! TASK
//! Implement `rwlock` as described in the stub.
//!
//! CONCEPT
//! RwLock allows many readers or one writer, good for read-heavy shared state.
//!
//! SIGNATURE
//! fn read() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::sync::RwLock;
fn read() -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/05-rwlock.rs"]
mod tests;