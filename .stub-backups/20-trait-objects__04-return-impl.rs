//! 20-trait-objects / 04-return-impl
//!
//! TASK
//! Return `impl Greet` from a factory function.
//!
//! SIGNATURE
//! fn make_greeter() -> impl Greet
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn make_greeter() -> impl Greet {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/04-return-impl.rs"]
mod tests;