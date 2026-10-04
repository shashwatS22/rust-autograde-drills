use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/t9", get(|| async { "trace" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/34-tower-and-tracing/checks/09-tower-9.rs"]
mod tests;
