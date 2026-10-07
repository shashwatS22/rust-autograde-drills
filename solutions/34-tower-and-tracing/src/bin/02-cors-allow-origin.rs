use axum::{routing::get, Router};
use tower_http::cors::{Any, CorsLayer};
pub fn app() -> Router {
    Router::new().route("/", get(|| async { "ok" })).layer(CorsLayer::new().allow_origin(Any))
}
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/34-tower-and-tracing/checks/02-cors-allow-origin.rs"]
mod tests;
