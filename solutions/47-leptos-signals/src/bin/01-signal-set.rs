use leptos::prelude::*;
fn after_set() -> i32 { let s = RwSignal::new(1); s.set(5); s.get() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/47-leptos-signals/checks/01-signal-set.rs"]
mod tests;
