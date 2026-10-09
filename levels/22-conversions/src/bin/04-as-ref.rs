//! 22-conversions / 04-as-ref
//!
//! TASK
//! Implement `as ref` as described in the stub.
//!
//! CONCEPT
//! AsRef<T> lets you accept anything that cheaply converts to a reference, like &str from String.
//!
//! SIGNATURE
//! fn len(s: impl AsRef<str>) -> usize
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn len(s: impl AsRef<str>) -> usize {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/04-as-ref.rs"]
mod tests;