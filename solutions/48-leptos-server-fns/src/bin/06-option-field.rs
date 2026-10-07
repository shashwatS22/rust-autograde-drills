use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct EchoReq { msg: Option<String> }
#[derive(Serialize, Deserialize)]
struct EchoResp { msg: String }
fn echo(req: EchoReq) -> EchoResp { EchoResp { msg: req.msg.unwrap_or_else(|| "none".into()) } }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/48-leptos-server-fns/checks/06-option-field.rs"]
mod tests;
