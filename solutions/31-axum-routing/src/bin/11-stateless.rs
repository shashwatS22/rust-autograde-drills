use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/r11", get(|| async { "ok" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/31-axum-routing/checks/11-stateless.rs"]
mod tests;
