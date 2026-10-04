use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/e2", get(|| async { "err" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/33-axum-errors/checks/02-error-2.rs"]
mod tests;
