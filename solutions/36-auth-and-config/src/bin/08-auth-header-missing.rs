use axum::{http::HeaderMap, routing::get, Router};
async fn me(headers: HeaderMap) -> Result<&'static str, axum::http::StatusCode> {
    match headers.get("authorization").and_then(|v| v.to_str().ok()) {
        Some("Bearer ok-token") => Ok("user"),
        _ => Err(axum::http::StatusCode::UNAUTHORIZED),
    }
}
pub fn app() -> Router { Router::new().route("/me", get(me)) }
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/36-auth-and-config/checks/08-auth-header-missing.rs"]
mod tests;
