use leptos::prelude::*;
#[component]
fn Card() -> impl IntoView { view! { <div class="card">ok</div> } }
fn render() -> String { view! { <Card/> }.into_view().to_html() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/46-leptos-components/checks/08-wrapper-class.rs"]
mod tests;
