//! 38-sync-primitives / 02-rwlock-readers
//!
//! TASK
//! Hold two read guards at once.
//!
//! SIGNATURE
//! fn many_reads() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::sync::RwLock;
fn many_reads() -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/02-rwlock-readers.rs"]
mod tests;
