use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/health", get(|| async { "healthy" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/31-axum-routing/checks/02-route-2.rs"]
mod tests;
