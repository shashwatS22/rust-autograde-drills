//! 34-tower-and-tracing / 05-tower-5
//!
//! TASK
//! Build `app()` with GET `/t5` returning `trace`.
//!
//! SIGNATURE
//! fn app() -> axum::Router
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/t5", get(|| async { "todo" }))
}

fn main() {}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/05-tower-5.rs"]
mod tests;
