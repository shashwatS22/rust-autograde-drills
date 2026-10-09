//! 25-error-design / 02-anyhow
//!
//! TASK
//! Use anyhow::Result.
//!
//! SIGNATURE
//! fn read_num(s: &str) -> anyhow::Result<i32>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn read_num(s: &str) -> anyhow::Result<i32> { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/02-anyhow.rs"]
mod tests;