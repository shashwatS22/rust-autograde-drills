//! 28-channels-and-sync / 06-once
//!
//! TASK
//! Implement `once` as described in the stub.
//!
//! SIGNATURE
//! fn once() -> &'static str
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::sync::OnceLock;
fn once() -> &'static str {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/06-once.rs"]
mod tests;
