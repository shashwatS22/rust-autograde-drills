//! 30-serde / 04-option-absent
//!
//! TASK
//! Deserialize missing optional field as `None`.
//!
//! SIGNATURE
//! fn nick() -> Option<String>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct User { name: String, nick: Option<String> }
fn nick() -> Option<String> { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/04-option-absent.rs"]
mod tests;
