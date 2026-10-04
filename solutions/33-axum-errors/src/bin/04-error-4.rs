use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/e4", get(|| async { "err" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/33-axum-errors/checks/04-error-4.rs"]
mod tests;
