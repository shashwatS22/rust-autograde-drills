use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize, PartialEq, Debug)]
struct User { name: String }
fn round() -> String { let u = User { name: "a".into() }; serde_json::to_string(&u).unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/30-serde/checks/01-json-roundtrip.rs"]
mod tests;
