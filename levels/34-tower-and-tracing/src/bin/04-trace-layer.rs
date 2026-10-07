//! 34-tower-and-tracing / 04-trace-layer
//!
//! TASK
//! Wrap the router with `tower_http::trace::TraceLayer`.
//!
//! SIGNATURE
//! fn app() -> axum::Router
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use axum::{routing::get, Router};
use tower_http::trace::TraceLayer;
pub fn app() -> Router { todo!() }
fn main() {}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/04-trace-layer.rs"]
mod tests;
