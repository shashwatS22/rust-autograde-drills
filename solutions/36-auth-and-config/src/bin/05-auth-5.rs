use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/auth5", get(|| async { "secure" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/36-auth-and-config/checks/05-auth-5.rs"]
mod tests;
