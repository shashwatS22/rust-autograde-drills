use axum::{routing::post, Json, Router};
use serde::Deserialize;
#[derive(Deserialize)]
struct In { n: i32 }
async fn handler(Json(b): Json<In>) -> String { b.n.to_string() }
pub fn app() -> Router { Router::new().route("/", post(handler)) }
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/32-axum-extractors/checks/02-extractor-2.rs"]
mod tests;
