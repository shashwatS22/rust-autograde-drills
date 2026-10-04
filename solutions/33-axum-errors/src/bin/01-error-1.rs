use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/e1", get(|| async { "err" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/33-axum-errors/checks/01-error-1.rs"]
mod tests;
