use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct User { name: String, nick: Option<String> }
fn nick() -> Option<String> { serde_json::from_str::<User>(r#"{"name":"a"}"#).unwrap().nick }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/30-serde/checks/04-option-absent.rs"]
mod tests;
