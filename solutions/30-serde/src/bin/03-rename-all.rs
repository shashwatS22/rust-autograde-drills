use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
struct User { first_name: String }
fn camel() -> String { serde_json::to_string(&User { first_name: "a".into() }).unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/30-serde/checks/03-rename-all.rs"]
mod tests;
