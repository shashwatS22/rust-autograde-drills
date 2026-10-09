//! 33-axum-errors / 04-status-only
//!
//! TASK
//! Use `(StatusCode, &str)` as `IntoResponse` without a custom enum.
//!
//! SIGNATURE
//! fn app() -> axum::Router
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use axum::{http::StatusCode, response::IntoResponse, routing::get, Router};
async fn gone() -> impl IntoResponse { todo!() }
pub fn app() -> Router { todo!() }
fn main() {}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/04-status-only.rs"]
mod tests;