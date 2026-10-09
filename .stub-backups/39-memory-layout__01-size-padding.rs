//! 39-memory-layout / 01-size-padding
//!
//! TASK
//! Struct size includes alignment padding.
//!
//! CONCEPT
//! std::mem::size_of includes alignment padding between struct fields.
//!
//! SIGNATURE
//! fn padded_size() -> usize
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn padded_size() -> usize {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-size-padding.rs"]
mod tests;