//! 46-leptos-components / 07-child-prop
//!
//! TASK
//! Pass a numeric prop to a child component.
//!
//! SIGNATURE
//! fn render() -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use leptos::prelude::*;
#[component]
fn N(n: i32) -> impl IntoView { view! { <em>{n}</em> } }
fn render() -> String { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/07-child-prop.rs"]
mod tests;