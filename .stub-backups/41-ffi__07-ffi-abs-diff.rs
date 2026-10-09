//! 41-ffi / 07-ffi-abs-diff
//!
//! TASK
//! Compute absolute difference using `add_int` with negation.
//!
//! SIGNATURE
//! fn abs_diff(a: i32, b: i32) -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
#[link(name = "native_add")]
unsafe extern "C" { fn add_int(a: i32, b: i32) -> i32; }
fn abs_diff(a: i32, b: i32) -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/07-ffi-abs-diff.rs"]
mod tests;