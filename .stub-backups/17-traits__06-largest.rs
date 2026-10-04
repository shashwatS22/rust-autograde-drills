//! 17-traits / 06-largest
//!
//! TASK
//! `largest` with trait bound.
//!
//! SIGNATURE
//! fn largest_i32(v: &[i32]) -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn largest<T: PartialOrd>(list: &[T]) -> &T { todo!() }
fn largest_i32(v: &[i32]) -> i32 { *largest(v) }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/06-largest.rs"]
mod tests;
