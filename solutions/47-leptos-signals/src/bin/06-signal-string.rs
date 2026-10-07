use leptos::prelude::*;
fn label() -> String { let s = RwSignal::new("a".to_string()); s.set("b".into()); s.get() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/47-leptos-signals/checks/06-signal-string.rs"]
mod tests;
