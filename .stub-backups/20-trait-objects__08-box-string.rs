//! 20-trait-objects / 08-box-string
//!
//! TASK
//! Implement `box string` as described in the stub.
//!
//! CONCEPT
//! Box<String> moves the string to the heap; deref coercions often let you use &str methods.
//!
//! SIGNATURE
//! fn boxed_str() -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn boxed_str() -> String {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-box-string.rs"]
mod tests;