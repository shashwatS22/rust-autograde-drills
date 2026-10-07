//! 32-axum-extractors / 01-path-id
//!
//! TASK
//! Extract `{id}` with `Path`.
//!
//! SIGNATURE
//! fn app() -> axum::Router
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use axum::{extract::Path, routing::get, Router};
async fn user(Path(id): Path<u32>) -> String { todo!() }
pub fn app() -> Router { Router::new().route("/users/{id}", get(user)) }
fn main() {}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-path-id.rs"]
mod tests;
