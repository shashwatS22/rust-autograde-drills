use leptos::prelude::*;
fn signal_val() -> i32 { let s = RwSignal::new(1); s.get() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/47-leptos-signals/checks/01-signal-1.rs"]
mod tests;
