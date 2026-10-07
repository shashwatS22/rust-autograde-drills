//! 30-serde / 05-vec-json
//!
//! TASK
//! Serialize a `Vec` field.
//!
//! SIGNATURE
//! fn tags_len() -> usize
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct Post { tags: Vec<String> }
fn tags_len() -> usize { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/05-vec-json.rs"]
mod tests;
