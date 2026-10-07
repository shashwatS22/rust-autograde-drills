use axum::{http::HeaderMap, routing::get, Router};
async fn echo(headers: HeaderMap) -> String { headers.get("x-token").and_then(|v| v.to_str().ok()).unwrap_or("").into() }
pub fn app() -> Router { Router::new().route("/", get(echo)) }
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/32-axum-extractors/checks/06-header-map.rs"]
mod tests;
