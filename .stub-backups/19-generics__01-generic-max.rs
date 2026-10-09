//! 19-generics / 01-generic-max
//!
//! TASK
//! Implement `generic max` as described in the stub.
//!
//! CONCEPT
//! fn max<T: PartialOrd>(a: T, b: T) shares one function across types that can be compared.
//!
//! SIGNATURE
//! fn max_i32(a: i32, b: i32) -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn max_i32(a: i32, b: i32) -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-generic-max.rs"]
mod tests;