//! 46-leptos-components / 01-prop-greet
//!
//! TASK
//! Component with a prop (function argument).
//!
//! SIGNATURE
//! fn render() -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use leptos::prelude::*;
#[component]
fn Greet(name: &'static str) -> impl IntoView { todo!() }
fn render() -> String { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-prop-greet.rs"]
mod tests;
