//! 38-sync-primitives / 07-mutex-poison-recover
//!
//! TASK
//! Use a `Mutex` guard to mutate in place.
//!
//! SIGNATURE
//! fn into_inner() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::sync::Mutex;
fn into_inner() -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/07-mutex-poison-recover.rs"]
mod tests;
