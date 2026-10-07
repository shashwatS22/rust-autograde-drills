//! 32-axum-extractors / 07-missing-field
//!
//! TASK
//! Missing JSON field yields 422.
//!
//! SIGNATURE
//! fn app() -> axum::Router
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use axum::{routing::post, Json, Router};
use serde::Deserialize;
#[derive(Deserialize)]
struct In { n: i32, m: i32 }
async fn handler(Json(_): Json<In>) -> &'static str { "ok" }
pub fn app() -> Router { Router::new().route("/", post(handler)) }
fn main() {}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/07-missing-field.rs"]
mod tests;
