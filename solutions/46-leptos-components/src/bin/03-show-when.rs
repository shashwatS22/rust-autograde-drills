use leptos::prelude::*;
fn render(show: bool) -> String { view! { <Show when=move || show fallback=|| view! { <p>no</p> }><p>yes</p></Show> }.into_view().to_html() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/46-leptos-components/checks/03-show-when.rs"]
mod tests;
