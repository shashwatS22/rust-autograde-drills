use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/e3", get(|| async { "err" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/33-axum-errors/checks/03-error-3.rs"]
mod tests;
