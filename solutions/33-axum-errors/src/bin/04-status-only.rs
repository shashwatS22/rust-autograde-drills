use axum::{http::StatusCode, response::IntoResponse, routing::get, Router};
async fn gone() -> impl IntoResponse { (StatusCode::GONE, "gone") }
pub fn app() -> Router { Router::new().route("/gone", get(gone)) }
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/33-axum-errors/checks/04-status-only.rs"]
mod tests;
