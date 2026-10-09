//! 24-smart-pointers / 07-cow
//!
//! TASK
//! Implement `cow` as described in the stub.
//!
//! CONCEPT
//! Cow is either borrowed or owned; clone-on-write avoids allocating until mutation.
//!
//! SIGNATURE
//! fn cow() -> usize
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::borrow::Cow;
fn cow() -> usize {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/07-cow.rs"]
mod tests;