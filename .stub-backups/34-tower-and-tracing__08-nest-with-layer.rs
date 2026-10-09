//! 34-tower-and-tracing / 08-nest-with-layer
//!
//! TASK
//! Nest a router and apply a layer only to the nested routes.
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
use axum::http::HeaderValue;
pub fn app() -> Router { todo!() }
fn main() {}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-nest-with-layer.rs"]
mod tests;