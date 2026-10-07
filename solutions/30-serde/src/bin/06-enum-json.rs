use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize, Debug, PartialEq)]
enum Msg { Ping, Pong }
fn kind() -> String { serde_json::to_string(&Msg::Ping).unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/30-serde/checks/06-enum-json.rs"]
mod tests;
