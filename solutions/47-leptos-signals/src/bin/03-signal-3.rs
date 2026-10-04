use leptos::prelude::*;
fn signal_val() -> i32 { let s = RwSignal::new(3); s.get() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/47-leptos-signals/checks/03-signal-3.rs"]
mod tests;
