use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/t8", get(|| async { "trace" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/34-tower-and-tracing/checks/08-tower-8.rs"]
mod tests;
