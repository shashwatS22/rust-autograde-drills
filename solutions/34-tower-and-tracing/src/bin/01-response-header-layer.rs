use axum::{routing::get, Router};
use tower::util::MapResponseLayer;
use axum::response::Response;
use axum::http::HeaderValue;
pub fn app() -> Router {
    Router::new().route("/", get(|| async { "hi" })).layer(MapResponseLayer::new(|mut res: Response| {
        res.headers_mut().insert("x-drill", HeaderValue::from_static("1"));
        res
    }))
}
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/34-tower-and-tracing/checks/01-response-header-layer.rs"]
mod tests;
