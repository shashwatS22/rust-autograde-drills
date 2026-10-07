use leptos::prelude::*;
#[component]
fn N(n: i32) -> impl IntoView { view! { <em>{n}</em> } }
fn render() -> String { view! { <N n=3/> }.into_view().to_html() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/46-leptos-components/checks/07-child-prop.rs"]
mod tests;
