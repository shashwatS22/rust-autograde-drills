use leptos::prelude::*;
fn render() -> String { let items = vec![1, 2]; view! { <ul>{items.into_iter().map(|n| view! { <li>{n}</li> }).collect_view()}</ul> }.into_view().to_html() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/46-leptos-components/checks/02-list-map.rs"]
mod tests;
