//! 20-trait-objects / 03-impl-trait-arg
//!
//! TASK
//! Implement `impl trait arg` as described in the stub.
//!
//! SIGNATURE
//! fn talk(s: &dyn Speak) -> &str
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn talk(s: &dyn Speak) -> &str {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/03-impl-trait-arg.rs"]
mod tests;
