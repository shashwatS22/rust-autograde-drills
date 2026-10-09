//! 24-smart-pointers / 05-box-recursive
//!
//! TASK
//! Implement `box recursive` as described in the stub.
//!
//! CONCEPT
//! Recursive structs need Box (or Rc) so the size is known; direct self-embedding is infinite size.
//!
//! SIGNATURE
//! fn head() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn head() -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/05-box-recursive.rs"]
mod tests;