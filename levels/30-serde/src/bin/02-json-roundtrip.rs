//! 30-serde / 02-json-roundtrip
//!
//! TASK
//! Implement `json roundtrip` as described in the stub.
//!
//! SIGNATURE
//! fn round() -> User
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize, PartialEq, Debug)]
struct User { name: String, age: u32 }
fn round() -> User {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/02-json-roundtrip.rs"]
mod tests;
