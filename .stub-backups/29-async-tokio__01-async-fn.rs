//! 29-async-tokio / 01-async-fn
//!
//! TASK
//! Async fn returning 7.
//!
//! CONCEPT
//! async fn returns a Future; nothing runs until you .await or block_on it on a runtime.
//!
//! SIGNATURE
//! async fn seven() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
async fn seven() -> i32 { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-async-fn.rs"]
mod tests;