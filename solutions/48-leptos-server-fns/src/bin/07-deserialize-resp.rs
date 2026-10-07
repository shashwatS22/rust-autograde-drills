use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct CountResp { n: i32 }
fn parse_resp() -> i32 { serde_json::from_str::<CountResp>("{\"n\":9}").unwrap().n }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/48-leptos-server-fns/checks/07-deserialize-resp.rs"]
mod tests;
