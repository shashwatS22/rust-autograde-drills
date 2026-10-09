//! 48-leptos-server-fns / 02-greet-contract
//!
//! TASK
//! String in, string out.
//!
//! SIGNATURE
//! fn greet(req: GreetReq) -> GreetResp
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct GreetReq { name: String }
#[derive(Serialize, Deserialize)]
struct GreetResp { msg: String }
fn greet(req: GreetReq) -> GreetResp { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/02-greet-contract.rs"]
mod tests;