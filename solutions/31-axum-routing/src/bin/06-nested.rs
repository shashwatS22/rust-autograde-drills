use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/nested", get(|| async { "n" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/31-axum-routing/checks/06-nested.rs"]
mod tests;
