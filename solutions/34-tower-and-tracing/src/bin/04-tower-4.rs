use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/t4", get(|| async { "trace" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/34-tower-and-tracing/checks/04-tower-4.rs"]
mod tests;
