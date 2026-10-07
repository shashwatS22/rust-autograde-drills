//! 34-tower-and-tracing / 02-cors-allow-origin
//!
//! TASK
//! Allow any origin with `tower_http::cors::CorsLayer`.
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
#[path = "../../checks/02-cors-allow-origin.rs"]
mod tests;
