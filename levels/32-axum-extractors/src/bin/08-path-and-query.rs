//! 32-axum-extractors / 08-path-and-query
//!
//! TASK
//! Combine `Path` and `Query`.
//!
//! SIGNATURE
//! fn app() -> axum::Router
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use axum::{extract::{Path, Query}, routing::get, Router};
use serde::Deserialize;
#[derive(Deserialize)]
struct Q { verbose: bool }
async fn show(Path(id): Path<u32>, Query(q): Query<Q>) -> String { todo!() }
pub fn app() -> Router { Router::new().route("/items/{id}", get(show)) }
fn main() {}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-path-and-query.rs"]
mod tests;