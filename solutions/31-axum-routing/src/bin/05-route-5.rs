use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/ping", get(|| async { "pong" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/31-axum-routing/checks/05-route-5.rs"]
mod tests;
