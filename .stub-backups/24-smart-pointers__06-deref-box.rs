//! 24-smart-pointers / 06-deref-box
//!
//! TASK
//! Implement `deref box` as described in the stub.
//!
//! CONCEPT
//! Deref on Box lets *box and method calls forward to the inner T.
//!
//! SIGNATURE
//! fn len() -> usize
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::ops::Deref;
fn len() -> usize {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/06-deref-box.rs"]
mod tests;