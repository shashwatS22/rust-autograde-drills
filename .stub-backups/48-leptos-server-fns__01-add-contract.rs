//! 48-leptos-server-fns / 01-add-contract
//!
//! TASK
//! Serde request/response pair (server-fn shape).
//!
//! CONCEPT
//! Server functions serialize request and response with Serde for the wire format.
//!
//! SIGNATURE
//! fn handle(req: AddReq) -> AddResp
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct AddReq { a: i32, b: i32 }
#[derive(Serialize, Deserialize)]
struct AddResp { sum: i32 }
fn handle(req: AddReq) -> AddResp { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-add-contract.rs"]
mod tests;