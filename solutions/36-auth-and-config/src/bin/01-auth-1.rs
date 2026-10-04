use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/auth1", get(|| async { "secure" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/36-auth-and-config/checks/01-auth-1.rs"]
mod tests;
