use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct User { #[serde(rename = "user_name")] name: String }
fn json_key() -> String { serde_json::to_string(&User { name: "x".into() }).unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/30-serde/checks/02-rename-field.rs"]
mod tests;
