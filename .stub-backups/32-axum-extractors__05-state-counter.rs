//! 32-axum-extractors / 05-state-counter
//!
//! TASK
//! Share handler state with `State`.
//!
//! SIGNATURE
//! fn app() -> axum::Router
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use axum::{extract::State, routing::get, Router};
use std::sync::Arc;
async fn count(State(n): State<Arc<i32>>) -> String { todo!() }
pub fn app() -> Router { Router::new().route("/", get(count)).with_state(Arc::new(5i32)) }
fn main() {}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/05-state-counter.rs"]
mod tests;
