use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/auth7", get(|| async { "secure" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/36-auth-and-config/checks/07-auth-7.rs"]
mod tests;
