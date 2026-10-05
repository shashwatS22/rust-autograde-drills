//! 25-error-design / 05-source-chain
//!
//! TASK
//! Implement `source chain` as described in the stub.
//!
//! SIGNATURE
//! fn err() -> Box<dyn Error>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::error::Error;
fn err() -> Box<dyn Error> {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/05-source-chain.rs"]
mod tests;
