use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/v1", get(|| async { "v1" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/31-axum-routing/checks/04-route-4.rs"]
mod tests;
