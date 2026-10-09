//! 28-channels-and-sync / 02-arc-mutex
//!
//! TASK
//! Implement `arc mutex` as described in the stub.
//!
//! CONCEPT
//! Arc shares ownership across threads; Mutex<T> protects inner data with lock().
//!
//! SIGNATURE
//! fn shared() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::sync::{Arc, Mutex};
use std::thread;
fn shared() -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/02-arc-mutex.rs"]
mod tests;