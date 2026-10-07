use leptos::prelude::*;
#[component]
fn Greet(name: &'static str) -> impl IntoView { view! { <p>{name}</p> } }
fn render() -> String { view! { <Greet name="Ada"/> }.into_view().to_html() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/46-leptos-components/checks/01-prop-greet.rs"]
mod tests;
