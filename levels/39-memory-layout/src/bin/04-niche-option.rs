//! 39-memory-layout / 04-niche-option
//!
//! TASK
//! `Option<NonZeroU8>` uses a niche (size 1).
//!
//! SIGNATURE
//! fn niche_one_byte() -> usize
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::num::NonZeroU8;
fn niche_one_byte() -> usize {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/04-niche-option.rs"]
mod tests;
