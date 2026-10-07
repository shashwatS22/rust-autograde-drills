use axum::{extract::{Path, Query}, routing::get, Router};
use serde::Deserialize;
#[derive(Deserialize)]
struct Q { verbose: bool }
async fn show(Path(id): Path<u32>, Query(q): Query<Q>) -> String { format!("{}:{}", id, q.verbose) }
pub fn app() -> Router { Router::new().route("/items/{id}", get(show)) }
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/32-axum-extractors/checks/08-path-and-query.rs"]
mod tests;
