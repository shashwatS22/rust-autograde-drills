use axum::{extract::Query, routing::get, Router};
use serde::Deserialize;
#[derive(Deserialize)]
struct Q { page: u32 }
async fn list(Query(q): Query<Q>) -> String { q.page.to_string() }
pub fn app() -> Router { Router::new().route("/list", get(list)) }
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/32-axum-extractors/checks/02-query-page.rs"]
mod tests;
