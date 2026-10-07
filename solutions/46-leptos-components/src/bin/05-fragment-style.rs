use leptos::prelude::*;
fn render() -> String { view! { <p>a</p><p>b</p> }.into_view().to_html() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/46-leptos-components/checks/05-fragment-style.rs"]
mod tests;
