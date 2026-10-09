//! 48-leptos-server-fns / 07-deserialize-resp
//!
//! TASK
//! Deserialize response JSON.
//!
//! SIGNATURE
//! fn parse_resp() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct CountResp { n: i32 }
fn parse_resp() -> i32 { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/07-deserialize-resp.rs"]
mod tests;