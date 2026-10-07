use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct PingReq { n: u32 }
fn round_json() -> String { serde_json::to_string(&PingReq { n: 1 }).unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/48-leptos-server-fns/checks/03-json-roundtrip.rs"]
mod tests;
