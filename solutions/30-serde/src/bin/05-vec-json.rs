use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct Post { tags: Vec<String> }
fn tags_len() -> usize { serde_json::from_str::<Post>("{\"tags\":[\"a\",\"b\"]}").unwrap().tags.len() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/30-serde/checks/05-vec-json.rs"]
mod tests;
