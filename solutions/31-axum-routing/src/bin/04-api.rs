use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/api", get(|| async { "api" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/31-axum-routing/checks/04-api.rs"]
mod tests;
