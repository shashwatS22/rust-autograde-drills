use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/auth8", get(|| async { "secure" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/36-auth-and-config/checks/08-auth-8.rs"]
mod tests;
