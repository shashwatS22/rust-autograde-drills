//! 21-lifetimes / 06-method
//!
//! TASK
//! Implement `method` as described in the stub.
//!
//! CONCEPT
//! Methods can return references tied to &self with the same lifetime as the impl block.
//!
//! SIGNATURE
//! fn g() -> &'static str
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn g() -> &'static str {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/06-method.rs"]
mod tests;