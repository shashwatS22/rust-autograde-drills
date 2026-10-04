//! 20-trait-objects / 06-count-dyn
//!
//! TASK
//! Complete `06-count-dyn` (count dyn).
//!
//! SIGNATURE
//! fn sum(v: &[Box<dyn Id>]) -> u32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn sum(v: &[Box<dyn Id>]) -> u32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/06-count-dyn.rs"]
mod tests;
