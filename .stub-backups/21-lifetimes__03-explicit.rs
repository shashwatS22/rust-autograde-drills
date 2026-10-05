//! 21-lifetimes / 03-explicit
//!
//! TASK
//! Implement `explicit` as described in the stub.
//!
//! SIGNATURE
//! fn identity<'a>(x: &'a str) -> &'a str
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn identity<'a>(x: &'a str) -> &'a str {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/03-explicit.rs"]
mod tests;
