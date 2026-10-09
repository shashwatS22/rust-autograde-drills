//! 21-lifetimes / 05-elision
//!
//! TASK
//! Implement `elision` as described in the stub.
//!
//! CONCEPT
//! Lifetime elision rules let you omit 'a on simple functions; the compiler fills them in.
//!
//! SIGNATURE
//! fn first(s: &str) -> &str
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn first(s: &str) -> &str {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/05-elision.rs"]
mod tests;