use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct GreetReq { name: String }
#[derive(Serialize, Deserialize)]
struct GreetResp { msg: String }
fn greet(req: GreetReq) -> GreetResp { GreetResp { msg: format!("Hello, {}!", req.name) } }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/48-leptos-server-fns/checks/02-greet-contract.rs"]
mod tests;
