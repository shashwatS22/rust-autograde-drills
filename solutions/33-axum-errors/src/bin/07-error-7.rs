use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/e7", get(|| async { "err" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/33-axum-errors/checks/07-error-7.rs"]
mod tests;
