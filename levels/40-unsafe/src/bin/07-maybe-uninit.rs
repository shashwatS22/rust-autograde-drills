//! 40-unsafe / 07-maybe-uninit
//!
//! TASK
//! Write into `MaybeUninit` then `assume_init`.
//!
//! SIGNATURE
//! fn init_on_stack() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::mem::MaybeUninit;
fn init_on_stack() -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/07-maybe-uninit.rs"]
mod tests;
