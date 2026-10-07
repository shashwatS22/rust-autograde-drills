use axum::{extract::Path, routing::get, Router};
async fn user(Path(id): Path<u32>) -> String { id.to_string() }
pub fn app() -> Router { Router::new().route("/users/{id}", get(user)) }
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/32-axum-extractors/checks/01-path-id.rs"]
mod tests;
