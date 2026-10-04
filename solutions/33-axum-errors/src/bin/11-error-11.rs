use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/e11", get(|| async { "err" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/33-axum-errors/checks/11-error-11.rs"]
mod tests;
