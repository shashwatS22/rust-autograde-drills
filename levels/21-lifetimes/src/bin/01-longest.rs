//! 21-lifetimes / 01-longest
//!
//! TASK
//! Implement `longest` as described in the stub.
//!
//! CONCEPT
//! Lifetime annotations like 'a tie two references: the returned &str cannot outlive the shorter input.
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