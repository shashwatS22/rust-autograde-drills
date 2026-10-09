//! 29-async-tokio / 04-spawn
//!
//! TASK
//! Implement `spawn` as described in the stub.
//!
//! CONCEPT
//! tokio::spawn runs a future on the runtime concurrently with the caller.
//!
//! SIGNATURE
//! async fn spawned() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
async fn spawned() -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/04-spawn.rs"]
mod tests;