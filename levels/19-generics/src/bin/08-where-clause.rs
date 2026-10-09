//! 19-generics / 08-where-clause
//!
//! TASK
//! Implement `where clause` as described in the stub.
//!
//! CONCEPT
//! where T: Trait syntax splits complex bounds onto their own line for readability.
//!
//! SIGNATURE
//! fn largest<T>(a: T, b: T) -> T
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn largest<T>(a: T, b: T) -> T {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-where-clause.rs"]
mod tests;