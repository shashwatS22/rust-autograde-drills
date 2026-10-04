use leptos::prelude::*;
fn signal_val() -> i32 { let s = RwSignal::new(6); s.get() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/47-leptos-signals/checks/06-signal-6.rs"]
mod tests;
