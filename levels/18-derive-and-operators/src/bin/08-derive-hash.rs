//! 18-derive-and-operators / 08-derive-hash
//!
//! TASK
//! Derive `Hash` and collect into a `HashSet`.
//!
//! SIGNATURE
//! fn uniq_keys() -> usize
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
#[derive(Hash, Eq, PartialEq)]
struct Key(i32);
use std::collections::HashSet;
fn uniq_keys() -> usize {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-derive-hash.rs"]
mod tests;