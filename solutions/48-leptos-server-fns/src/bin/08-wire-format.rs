use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct OkResp { ok: bool }
fn wire() -> String { serde_json::to_string(&OkResp { ok: true }).unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/48-leptos-server-fns/checks/08-wire-format.rs"]
mod tests;
