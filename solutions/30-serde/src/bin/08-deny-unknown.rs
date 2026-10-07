use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
struct User { name: String }
fn strict_err() -> bool { serde_json::from_str::<User>(r#"{"name":"a","extra":1}"#).is_err() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/30-serde/checks/08-deny-unknown.rs"]
mod tests;
