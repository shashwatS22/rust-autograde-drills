//! 48-leptos-server-fns / 03-json-roundtrip
//!
//! TASK
//! Round-trip the request type through JSON.
//!
//! SIGNATURE
//! fn round_json() -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct PingReq { n: u32 }
fn round_json() -> String { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/03-json-roundtrip.rs"]
mod tests;