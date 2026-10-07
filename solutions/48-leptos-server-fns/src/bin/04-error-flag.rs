use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct AuthReq { token: String }
#[derive(Serialize, Deserialize)]
struct AuthResp { ok: bool }
fn auth(req: AuthReq) -> AuthResp { AuthResp { ok: req.token == "good" } }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/48-leptos-server-fns/checks/04-error-flag.rs"]
mod tests;
