use leptos::prelude::*;
fn signal_val() -> i32 { let s = RwSignal::new(8); s.get() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/47-leptos-signals/checks/08-signal-8.rs"]
mod tests;
