use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/t7", get(|| async { "trace" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/34-tower-and-tracing/checks/07-tower-7.rs"]
mod tests;
