//! 27-threads / 02-move-closure
//!
//! TASK
//! Implement `move closure` as described in the stub.
//!
//! CONCEPT
//! move || { ... } on spawn transfers captured variables into the new thread.
//!
//! SIGNATURE
//! fn moved() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::thread;
fn moved() -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/02-move-closure.rs"]
mod tests;