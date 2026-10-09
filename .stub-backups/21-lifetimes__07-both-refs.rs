//! 21-lifetimes / 07-both-refs
//!
//! TASK
//! Implement `both refs` as described in the stub.
//!
//! CONCEPT
//! When two inputs share 'a, the result must not outlive either borrowed value.
//!
//! SIGNATURE
//! fn both<'a>(a: &'a str, b: &'a str) -> (&'a str, &'a str)
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn both<'a>(a: &'a str, b: &'a str) -> (&'a str, &'a str) {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/07-both-refs.rs"]
mod tests;