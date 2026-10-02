//! 08-functions / 07-apply-twice
//!
//! TASK
//! Complete `07-apply-twice` per the level README and spec.
//!
//! SIGNATURE
//! fn apply_twice(f: impl Fn(i32) -> i32, value: i32) -> i32
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
