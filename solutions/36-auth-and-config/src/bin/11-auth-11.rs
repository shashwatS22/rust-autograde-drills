use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/auth11", get(|| async { "secure" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/36-auth-and-config/checks/11-auth-11.rs"]
mod tests;
