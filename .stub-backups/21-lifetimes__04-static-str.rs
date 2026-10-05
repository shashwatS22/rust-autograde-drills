//! 21-lifetimes / 04-static-str
//!
//! TASK
//! Implement `static str` as described in the stub.
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
