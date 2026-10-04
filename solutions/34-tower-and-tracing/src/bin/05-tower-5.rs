use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/t5", get(|| async { "trace" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/34-tower-and-tracing/checks/05-tower-5.rs"]
mod tests;
