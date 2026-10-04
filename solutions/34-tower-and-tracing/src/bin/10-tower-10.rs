use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/t10", get(|| async { "trace" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/34-tower-and-tracing/checks/10-tower-10.rs"]
mod tests;
