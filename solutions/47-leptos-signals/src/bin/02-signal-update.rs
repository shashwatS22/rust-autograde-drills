use leptos::prelude::*;
fn after_update() -> i32 { let s = RwSignal::new(2); s.update(|n| *n += 3); s.get() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/47-leptos-signals/checks/02-signal-update.rs"]
mod tests;
