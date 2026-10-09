//! 46-leptos-components / 04-nested-components
//!
//! TASK
//! Nest two components.
//!
//! SIGNATURE
//! fn render() -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use leptos::prelude::*;
#[component]
fn Inner() -> impl IntoView { todo!() }
#[component]
fn Outer() -> impl IntoView { view! { <Inner/> } }
fn render() -> String { view! { <Outer/> }.into_view().to_html() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/04-nested-components.rs"]
mod tests;