use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct AddReq { a: i32, b: i32 }
#[derive(Serialize, Deserialize)]
struct AddResp { sum: i32 }
fn handle(req: AddReq) -> AddResp { AddResp { sum: req.a + req.b } }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/48-leptos-server-fns/checks/01-add-contract.rs"]
mod tests;
