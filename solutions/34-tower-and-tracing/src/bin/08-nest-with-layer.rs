use axum::{routing::get, Router};
use tower::util::MapResponseLayer;
use axum::response::Response;
use axum::http::HeaderValue;
pub fn app() -> Router {
    let api = Router::new().route("/inner", get(|| async { "in" })).layer(MapResponseLayer::new(|mut res: Response| {
        res.headers_mut().insert("x-nested", HeaderValue::from_static("1")); res
    }));
    Router::new().nest("/api", api)
}
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/34-tower-and-tracing/checks/08-nest-with-layer.rs"]
mod tests;
