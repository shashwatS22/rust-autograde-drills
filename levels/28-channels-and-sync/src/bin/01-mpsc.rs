//! 28-channels-and-sync / 01-mpsc
//!
//! TASK
//! Implement `mpsc` as described in the stub.
//!
//! CONCEPT
//! mpsc channels send messages between threads; the sender clone shares one receiver.
//!
//! SIGNATURE
//! fn send_recv() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::sync::mpsc;
fn send_recv() -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-mpsc.rs"]
mod tests;