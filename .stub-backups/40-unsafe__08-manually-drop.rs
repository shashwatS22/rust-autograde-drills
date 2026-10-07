//! 40-unsafe / 08-manually-drop
//!
//! TASK
//! Use `ManuallyDrop` to control drop order.
//!
//! SIGNATURE
//! fn no_double_free() -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::mem::ManuallyDrop;
fn no_double_free() -> String {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-manually-drop.rs"]
mod tests;
