use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/e10", get(|| async { "err" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/33-axum-errors/checks/10-error-10.rs"]
mod tests;
