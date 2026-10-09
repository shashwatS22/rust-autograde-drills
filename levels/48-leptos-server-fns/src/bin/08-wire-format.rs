//! 48-leptos-server-fns / 08-wire-format
//!
//! TASK
//! Serialize response for wire format.
//!
//! SIGNATURE
//! fn wire() -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct OkResp { ok: bool }
fn wire() -> String { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-wire-format.rs"]
mod tests;