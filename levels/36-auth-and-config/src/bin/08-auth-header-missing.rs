//! 36-auth-and-config / 08-auth-header-missing
//!
//! TASK
//! Missing `Authorization` returns 401.
//!
//! SIGNATURE
//! fn app() -> axum::Router
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use axum::{http::HeaderMap, routing::get, Router};
async fn me(headers: HeaderMap) -> Result<&'static str, axum::http::StatusCode> { todo!() }
pub fn app() -> Router { todo!() }
fn main() {}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-auth-header-missing.rs"]
mod tests;
