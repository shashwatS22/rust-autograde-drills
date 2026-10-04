use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/t2", get(|| async { "trace" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/34-tower-and-tracing/checks/02-tower-2.rs"]
mod tests;
