//! 48-leptos-server-fns / 04-error-flag
//!
//! TASK
//! Response includes success flag.
//!
//! SIGNATURE
//! fn auth(req: AuthReq) -> AuthResp
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct AuthReq { token: String }
#[derive(Serialize, Deserialize)]
struct AuthResp { ok: bool }
fn auth(req: AuthReq) -> AuthResp { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/04-error-flag.rs"]
mod tests;