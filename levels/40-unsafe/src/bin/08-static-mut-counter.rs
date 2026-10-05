//! 40-unsafe / 08-static-mut-counter
//!
//! TASK
//! Increment a `static mut` counter inside `unsafe` (tests run serially).
//!
//! SIGNATURE
//! fn bump_unsafe() -> u32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn bump_unsafe() -> u32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-static-mut-counter.rs"]
mod tests;
