use leptos::prelude::*;
#[component]
fn Inner() -> impl IntoView { view! { <span>in</span> } }
#[component]
fn Outer() -> impl IntoView { view! { <div><Inner/></div> } }
fn render() -> String { view! { <Outer/> }.into_view().to_html() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/46-leptos-components/checks/04-nested-components.rs"]
mod tests;
