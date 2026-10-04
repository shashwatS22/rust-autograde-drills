use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/t3", get(|| async { "trace" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/34-tower-and-tracing/checks/03-tower-3.rs"]
mod tests;
