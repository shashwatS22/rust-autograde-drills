use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/any", get(|| async { "fallback" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/31-axum-routing/checks/07-fallback.rs"]
mod tests;
