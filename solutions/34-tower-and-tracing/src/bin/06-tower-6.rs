use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/t6", get(|| async { "trace" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/34-tower-and-tracing/checks/06-tower-6.rs"]
mod tests;
