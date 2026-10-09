//! 46-leptos-components / 08-wrapper-class
//!
//! TASK
//! Wrapper component adds a CSS class name in markup.
//!
//! SIGNATURE
//! fn render() -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use leptos::prelude::*;
#[component]
fn Card() -> impl IntoView { view! { <div class="card">ok</div> } }
fn render() -> String { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-wrapper-class.rs"]
mod tests;