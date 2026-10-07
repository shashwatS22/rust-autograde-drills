//! 33-axum-errors / 05-json-error-body
//!
//! TASK
//! Return JSON error body with `(StatusCode, Json<_>)`.
//!
//! SIGNATURE
//! fn app() -> axum::Router
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use axum::{http::StatusCode, response::IntoResponse, routing::get, Json, Router};
use serde::Serialize;
#[derive(Serialize)]
struct ErrBody { msg: &'static str }
async fn fail() -> impl IntoResponse { todo!() }
pub fn app() -> Router { todo!() }
fn main() {}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/05-json-error-body.rs"]
mod tests;
