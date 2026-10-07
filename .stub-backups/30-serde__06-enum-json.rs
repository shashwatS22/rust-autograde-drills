//! 30-serde / 06-enum-json
//!
//! TASK
//! Externally tagged enum in JSON.
//!
//! SIGNATURE
//! fn kind() -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize, Debug, PartialEq)]
enum Msg { Ping, Pong }
fn kind() -> String { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/06-enum-json.rs"]
mod tests;
