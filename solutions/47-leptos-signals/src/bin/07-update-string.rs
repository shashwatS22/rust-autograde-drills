use leptos::prelude::*;
fn len() -> usize { let s = RwSignal::new(String::new()); s.update(|t| t.push_str("hi")); s.get().len() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/47-leptos-signals/checks/07-update-string.rs"]
mod tests;
