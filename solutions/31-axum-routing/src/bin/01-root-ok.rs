use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/", get(|| async { "ok" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/31-axum-routing/checks/01-root-ok.rs"]
mod tests;
