//! 34-tower-and-tracing / 06-layer-stack
//!
//! TASK
//! Stack CORS and a custom response header layer.
//!
//! SIGNATURE
//! fn app() -> axum::Router
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use axum::{routing::get, Router};
use tower::util::MapResponseLayer;
use tower_http::cors::{Any, CorsLayer};
use axum::response::Response;
use axum::http::HeaderValue;
pub fn app() -> Router { todo!() }
fn main() {}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/06-layer-stack.rs"]
mod tests;