use axum::{routing::get, Router};
use tower_http::trace::TraceLayer;
pub fn app() -> Router {
    Router::new().route("/ping", get(|| async { "pong" })).layer(TraceLayer::new_for_http())
}
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/34-tower-and-tracing/checks/04-trace-layer.rs"]
mod tests;
