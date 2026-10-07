use leptos::prelude::*;
fn render(n: i32) -> String { view! { <p>{n}</p> }.into_view().to_html() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/46-leptos-components/checks/06-dynamic-tag-text.rs"]
mod tests;
