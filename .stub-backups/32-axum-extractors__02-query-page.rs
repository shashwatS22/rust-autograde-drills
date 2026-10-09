//! 32-axum-extractors / 02-query-page
//!
//! TASK
//! Extract query string with `Query`.
//!
//! SIGNATURE
//! fn app() -> axum::Router
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use axum::{extract::Query, routing::get, Router};
use serde::Deserialize;
#[derive(Deserialize)]
struct Q { page: u32 }
async fn list(Query(q): Query<Q>) -> String { todo!() }
pub fn app() -> Router { Router::new().route("/list", get(list)) }
fn main() {}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/02-query-page.rs"]
mod tests;