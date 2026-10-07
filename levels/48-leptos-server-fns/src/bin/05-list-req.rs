//! 48-leptos-server-fns / 05-list-req
//!
//! TASK
//! Request carries a `Vec`.
//!
//! SIGNATURE
//! fn total(req: SumReq) -> SumResp
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct SumReq { values: Vec<i32> }
#[derive(Serialize, Deserialize)]
struct SumResp { total: i32 }
fn total(req: SumReq) -> SumResp { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/05-list-req.rs"]
mod tests;
