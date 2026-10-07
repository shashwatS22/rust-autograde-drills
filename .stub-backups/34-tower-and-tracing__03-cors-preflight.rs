//! 34-tower-and-tracing / 03-cors-preflight
//!
//! TASK
//! Answer an OPTIONS preflight with CORS headers.
//!
//! SIGNATURE
//! fn app() -> axum::Router
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use axum::{routing::get, Router};
use tower_http::cors::{Any, CorsLayer};
pub fn app() -> Router { todo!() }
fn main() {}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/03-cors-preflight.rs"]
mod tests;
