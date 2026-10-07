use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct Score { #[serde(default)] points: u32 }
fn score_default() -> u32 { serde_json::from_str::<Score>("{}").unwrap().points }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/30-serde/checks/07-default-field.rs"]
mod tests;
