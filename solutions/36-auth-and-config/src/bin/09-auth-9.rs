use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/auth9", get(|| async { "secure" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/36-auth-and-config/checks/09-auth-9.rs"]
mod tests;
