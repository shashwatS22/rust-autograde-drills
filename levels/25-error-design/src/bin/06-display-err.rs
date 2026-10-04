//! 25-error-design / 06-display-err
//!
//! TASK
//! Complete `06-display-err` (display err).
//!
//! SIGNATURE
//! fn msg() -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use thiserror::Error;
#[derive(Error, Debug)]
#[error("code {0}")]
struct E(u32);
fn msg() -> String {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/06-display-err.rs"]
mod tests;
