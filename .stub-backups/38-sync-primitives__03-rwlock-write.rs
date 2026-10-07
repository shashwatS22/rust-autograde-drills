//! 38-sync-primitives / 03-rwlock-write
//!
//! TASK
//! Take a write lock, then read the new value.
//!
//! SIGNATURE
//! fn write_bump() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::sync::RwLock;
fn write_bump() -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/03-rwlock-write.rs"]
mod tests;
