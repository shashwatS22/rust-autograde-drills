use leptos::prelude::*;
fn signal_val() -> i32 { let s = RwSignal::new(4); s.get() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/47-leptos-signals/checks/04-signal-4.rs"]
mod tests;
