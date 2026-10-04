//! 25-error-design / 04-context
//!
//! TASK
//! Complete `04-context` (context).
//!
//! SIGNATURE
//! fn ctx(s: &str) -> anyhow::Result<i32>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use anyhow::Context;
fn ctx(s: &str) -> anyhow::Result<i32> {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/04-context.rs"]
mod tests;
