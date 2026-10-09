//! 40-unsafe / 01-ptr-read
//!
//! TASK
//! Read a `u8` through a raw pointer (stack value must stay valid).
//!
//! CONCEPT
//! unsafe blocks allow raw pointer reads; the pointed-to value must stay valid for the read.
//!
//! SIGNATURE
//! fn read_byte() -> u8
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn read_byte() -> u8 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-ptr-read.rs"]
mod tests;