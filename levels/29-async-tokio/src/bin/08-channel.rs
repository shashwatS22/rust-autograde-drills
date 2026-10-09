//! 29-async-tokio / 08-channel
//!
//! TASK
//! Implement `channel` as described in the stub.
//!
//! CONCEPT
//! tokio::sync::mpsc is an async channel: send and recv are .await points.
//!
//! SIGNATURE
//! async fn chan() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
async fn chan() -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-channel.rs"]
mod tests;