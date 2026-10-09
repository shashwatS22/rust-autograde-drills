//! 21-lifetimes / 04-static-str
//!
//! TASK
//! Implement `static str` as described in the stub.
//!
//! CONCEPT
//! 'static means the reference lives for the entire program, like string literals.
//!
//! SIGNATURE
//! fn msg() -> &'static str
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn msg() -> &'static str {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/04-static-str.rs"]
mod tests;