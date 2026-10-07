use axum::{routing::get, Router};
use tower::util::MapResponseLayer;
use tower_http::cors::{Any, CorsLayer};
use axum::response::Response;
use axum::http::HeaderValue;
pub fn app() -> Router {
    Router::new().route("/", get(|| async { "x" }))
        .layer(CorsLayer::new().allow_origin(Any))
        .layer(MapResponseLayer::new(|mut res: Response| { res.headers_mut().insert("x-stack", HeaderValue::from_static("yes")); res }))
}
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/34-tower-and-tracing/checks/06-layer-stack.rs"]
mod tests;
