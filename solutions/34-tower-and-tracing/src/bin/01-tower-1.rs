use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/t1", get(|| async { "trace" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/34-tower-and-tracing/checks/01-tower-1.rs"]
mod tests;
