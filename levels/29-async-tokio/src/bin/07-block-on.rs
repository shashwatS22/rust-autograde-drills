//! 29-async-tokio / 07-block-on
//!
//! TASK
//! Implement `block on` as described in the stub.
//!
//! CONCEPT
//! block_on runs an async block on the current runtime from synchronous code (tests only here).
//!
//! SIGNATURE
//! fn sync() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn sync() -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/07-block-on.rs"]
mod tests;