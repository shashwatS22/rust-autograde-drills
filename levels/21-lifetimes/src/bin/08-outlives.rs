//! 21-lifetimes / 08-outlives
//!
//! TASK
//! Implement `outlives` as described in the stub.
//!
//! CONCEPT
//! choose returns one of two references with the same 'a: both must live equally long.
//!
//! SIGNATURE
//! fn choose<'a>(flag: bool, a: &'a str, b: &'a str) -> &'a str
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn choose<'a>(flag: bool, a: &'a str, b: &'a str) -> &'a str {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-outlives.rs"]
mod tests;