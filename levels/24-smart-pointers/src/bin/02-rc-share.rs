//! 24-smart-pointers / 02-rc-share
//!
//! TASK
//! Implement `rc share` as described in the stub.
//!
//! CONCEPT
//! Rc<T> is reference-counted shared ownership for single-threaded code.
//!
//! SIGNATURE
//! fn shared() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::rc::Rc;
fn shared() -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/02-rc-share.rs"]
mod tests;