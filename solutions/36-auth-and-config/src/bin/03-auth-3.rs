use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/auth3", get(|| async { "secure" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/36-auth-and-config/checks/03-auth-3.rs"]
mod tests;
