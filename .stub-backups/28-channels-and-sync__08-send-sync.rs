//! 28-channels-and-sync / 08-send-sync
//!
//! TASK
//! Implement `send sync` as described in the stub.
//!
//! SIGNATURE
//! fn is_send<T: Send>() -> bool
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn is_send<T: Send>() -> bool {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-send-sync.rs"]
mod tests;
