//! 34-tower-and-tracing / 01-response-header-layer
//!
//! TASK
//! Add a response header with `tower::util::MapResponseLayer`.
//!
//! CONCEPT
//! Tower layers wrap services; MapResponseLayer transforms responses as they pass through.
//!
//! SIGNATURE
//! fn app() -> axum::Router
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use axum::{routing::get, Router};
use tower::util::MapResponseLayer;
use axum::response::Response;
pub fn app() -> Router { todo!() }
fn main() {}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-response-header-layer.rs"]
mod tests;