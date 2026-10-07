//! 32-axum-extractors / 03-json-body
//!
//! TASK
//! Parse JSON body with `Json`.
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
struct In { n: i32 }
async fn handler(Json(b): Json<In>) -> String { todo!() }
pub fn app() -> Router { Router::new().route("/", post(handler)) }
fn main() {}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/03-json-body.rs"]
mod tests;
