use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/e6", get(|| async { "err" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/33-axum-errors/checks/06-error-6.rs"]
mod tests;
