//! 21-lifetimes / 01-longest
//!
//! TASK
//! Complete `01-longest` (longest).
//!
//! SIGNATURE
//! fn longest<'a>(a: &'a str, b: &'a str) -> &'a str
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn longest<'a>(a: &'a str, b: &'a str) -> &'a str {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-longest.rs"]
mod tests;
