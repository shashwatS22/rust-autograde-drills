//! 48-leptos-server-fns / 06-option-field
//!
//! TASK
//! Optional field in request.
//!
//! SIGNATURE
//! fn echo(req: EchoReq) -> EchoResp
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct EchoReq { msg: Option<String> }
#[derive(Serialize, Deserialize)]
struct EchoResp { msg: String }
fn echo(req: EchoReq) -> EchoResp { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/06-option-field.rs"]
mod tests;
