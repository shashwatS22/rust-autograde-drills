//! 30-serde / 08-deny-unknown
//!
//! TASK
//! Reject unknown JSON keys with `deny_unknown_fields`.
//!
//! SIGNATURE
//! fn strict_err() -> bool
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
struct User { name: String }
fn strict_err() -> bool { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-deny-unknown.rs"]
mod tests;
