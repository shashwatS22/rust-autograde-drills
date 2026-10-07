//! 32-axum-extractors / 06-header-map
//!
//! TASK
//! Read a request header.
//!
//! SIGNATURE
//! fn app() -> axum::Router
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use axum::{http::HeaderMap, routing::get, Router};
async fn echo(headers: HeaderMap) -> String { todo!() }
pub fn app() -> Router { Router::new().route("/", get(echo)) }
fn main() {}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/06-header-map.rs"]
mod tests;
