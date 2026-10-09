//! 30-serde / 01-json-roundtrip
//!
//! TASK
//! Derive Serialize/Deserialize and round-trip JSON.
//!
//! CONCEPT
//! #[derive(Serialize, Deserialize)] lets serde_json turn structs into JSON strings and back.
//!
//! SIGNATURE
//! fn round() -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize, PartialEq, Debug)]
struct User { name: String }
fn round() -> String { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-json-roundtrip.rs"]
mod tests;