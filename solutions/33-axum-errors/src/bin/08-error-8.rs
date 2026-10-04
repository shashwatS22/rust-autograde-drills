use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/e8", get(|| async { "err" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/33-axum-errors/checks/08-error-8.rs"]
mod tests;
