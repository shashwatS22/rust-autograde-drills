use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct SumReq { values: Vec<i32> }
#[derive(Serialize, Deserialize)]
struct SumResp { total: i32 }
fn total(req: SumReq) -> SumResp { SumResp { total: req.values.iter().sum() } }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/48-leptos-server-fns/checks/05-list-req.rs"]
mod tests;
