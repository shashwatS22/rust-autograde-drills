use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/e5", get(|| async { "err" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/33-axum-errors/checks/05-error-5.rs"]
mod tests;
