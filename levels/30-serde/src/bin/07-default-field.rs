//! 30-serde / 07-default-field
//!
//! TASK
//! Fill missing fields with `#[serde(default)]`.
//!
//! SIGNATURE
//! fn score_default() -> u32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct Score { #[serde(default)] points: u32 }
fn score_default() -> u32 { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/07-default-field.rs"]
mod tests;