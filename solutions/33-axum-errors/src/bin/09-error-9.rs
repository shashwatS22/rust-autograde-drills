use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/e9", get(|| async { "err" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/33-axum-errors/checks/09-error-9.rs"]
mod tests;
