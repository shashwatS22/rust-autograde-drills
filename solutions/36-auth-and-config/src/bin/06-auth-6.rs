use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/auth6", get(|| async { "secure" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/36-auth-and-config/checks/06-auth-6.rs"]
mod tests;
