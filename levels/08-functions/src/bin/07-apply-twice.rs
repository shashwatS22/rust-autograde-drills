//! 08-functions / 07-apply-twice
//!
//! TASK
//! `fn apply_twice(f: impl Fn(i32) -> i32, value: i32) -> i32` returning `f(f(value))`.
//!
//! CONCEPT
//! impl Fn(i32) -> i32 means any callable that takes i32 and returns i32, including closures and function pointers.
//!
//! SIGNATURE
//! fn apply_twice(f: impl Fn(i32) -> i32, value: i32) -> i32` returning `f(f(value))`
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn apply_twice(f: impl Fn(i32) -> i32, value: i32) -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/07-apply-twice.rs"]
mod tests;