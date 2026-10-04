//! 31-axum-routing / 11-stateless
//!
//! TASK
//! Build `app()` with GET `/r11` returning `ok`.
//!
//! SIGNATURE
//! fn app() -> axum::Router
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use axum::{routing::get, Router};

pub fn app() -> Router {
    Router::new().route("/r11", get(|| async { "todo" }))
}

fn main() {}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/11-stateless.rs"]
mod tests;
