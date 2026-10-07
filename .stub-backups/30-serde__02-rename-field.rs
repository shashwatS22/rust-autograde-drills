//! 30-serde / 02-rename-field
//!
//! TASK
//! Use `#[serde(rename = "...")]` on one field.
//!
//! SIGNATURE
//! fn json_key() -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct User { #[serde(rename = "user_name")] name: String }
fn json_key() -> String { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/02-rename-field.rs"]
mod tests;
