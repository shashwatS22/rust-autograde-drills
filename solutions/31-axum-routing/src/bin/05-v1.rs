use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/v1", get(|| async { "v1" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/31-axum-routing/checks/05-v1.rs"]
mod tests;
