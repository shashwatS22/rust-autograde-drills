use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/auth4", get(|| async { "secure" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/36-auth-and-config/checks/04-auth-4.rs"]
mod tests;
