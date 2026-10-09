//! 31-axum-routing / 01-root-ok
//!
//! TASK
//! Build `app()` with GET `/` returning `ok`.
//!
//! CONCEPT
//! Router::new().route(path, get(handler)) wires HTTP paths to async handler functions.
//!
//! SIGNATURE
//! fn app() -> axum::Router
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/", get(|| async { "todo" }))
}

fn main() {}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-root-ok.rs"]
mod tests;