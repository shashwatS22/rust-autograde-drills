use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/get", get(|| async { "ok" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/31-axum-routing/checks/08-method-get.rs"]
mod tests;
