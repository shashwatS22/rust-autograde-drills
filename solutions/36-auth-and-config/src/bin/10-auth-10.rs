use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/auth10", get(|| async { "secure" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/36-auth-and-config/checks/10-auth-10.rs"]
mod tests;
