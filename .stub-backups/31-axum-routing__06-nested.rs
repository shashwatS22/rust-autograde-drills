//! 31-axum-routing / 06-nested
//!
//! TASK
//! Build `app()` with GET `/nested` returning `n`.
//!
//! SIGNATURE
//! fn app() -> axum::Router
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/nested", get(|| async { "todo" }))
}

fn main() {}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/06-nested.rs"]
mod tests;