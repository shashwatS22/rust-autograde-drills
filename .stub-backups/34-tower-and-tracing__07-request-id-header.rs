//! 34-tower-and-tracing / 07-request-id-header
//!
//! TASK
//! Echo `x-request-id` after layers are applied.
//!
//! SIGNATURE
//! fn app() -> axum::Router
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use axum::{http::HeaderMap, routing::get, Router};
async fn echo(headers: HeaderMap) -> String { todo!() }
pub fn app() -> Router { todo!() }
fn main() {}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/07-request-id-header.rs"]
mod tests;