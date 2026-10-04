use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize, PartialEq, Debug)]
struct User { name: String, age: u32 }
fn round() -> User { let u = User { name: "a".into(), age: 1 }; let j = serde_json::to_string(&u).unwrap(); serde_json::from_str(&j).unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/30-serde/checks/06-enum-json.rs"]
mod tests;
