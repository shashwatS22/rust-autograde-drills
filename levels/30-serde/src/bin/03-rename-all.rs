//! 30-serde / 03-rename-all
//!
//! TASK
//! Use `#[serde(rename_all = "camelCase")]`.
//!
//! SIGNATURE
//! fn camel() -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
struct User { first_name: String }
fn camel() -> String { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/03-rename-all.rs"]
mod tests;
