use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/r10", get(|| async { "ok" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/31-axum-routing/checks/10-merge.rs"]
mod tests;
