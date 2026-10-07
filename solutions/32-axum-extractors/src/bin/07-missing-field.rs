use axum::{routing::post, Json, Router};
use serde::Deserialize;
#[derive(Deserialize)]
struct In { n: i32, m: i32 }
async fn handler(Json(_): Json<In>) -> &'static str { "ok" }
pub fn app() -> Router { Router::new().route("/", post(handler)) }
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/32-axum-extractors/checks/07-missing-field.rs"]
mod tests;
