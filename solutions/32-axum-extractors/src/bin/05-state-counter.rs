use axum::{extract::State, routing::get, Router};
use std::sync::Arc;
async fn count(State(n): State<Arc<i32>>) -> String { n.to_string() }
pub fn app() -> Router { Router::new().route("/", get(count)).with_state(Arc::new(5i32)) }
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/32-axum-extractors/checks/05-state-counter.rs"]
mod tests;
