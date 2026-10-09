//! 29-async-tokio / 03-join
//!
//! TASK
//! Implement `join` as described in the stub.
//!
//! CONCEPT
//! join! or JoinHandle waits for multiple futures to complete.
//!
//! SIGNATURE
//! async fn both() -> (i32, i32)
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
async fn both() -> (i32, i32) {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/03-join.rs"]
mod tests;