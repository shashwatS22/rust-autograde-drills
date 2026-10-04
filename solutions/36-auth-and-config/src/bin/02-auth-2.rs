use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/auth2", get(|| async { "secure" }))
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/36-auth-and-config/checks/02-auth-2.rs"]
mod tests;
