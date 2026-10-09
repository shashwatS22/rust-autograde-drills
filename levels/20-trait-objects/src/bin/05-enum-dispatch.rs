//! 20-trait-objects / 05-enum-dispatch
//!
//! TASK
//! Implement `enum dispatch` as described in the stub.
//!
//! CONCEPT
//! Enums can implement traits by matching on variants, an alternative to dyn for known sets of types.
//!
//! SIGNATURE
//! fn sound(p: Pet) -> &'static str
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn sound(p: Pet) -> &'static str {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/05-enum-dispatch.rs"]
mod tests;