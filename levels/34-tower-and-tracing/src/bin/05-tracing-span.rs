//! 34-tower-and-tracing / 05-tracing-span
//!
//! TASK
//! Enter a `tracing` span inside a handler.
//!
//! SIGNATURE
//! fn app() -> axum::Router
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use axum::{routing::get, Router};
async fn traced() -> &'static str { todo!() }
pub fn app() -> Router { todo!() }
fn main() {}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/05-tracing-span.rs"]
mod tests;
