use leptos::prelude::*;
fn signal_val() -> i32 { let s = RwSignal::new(7); s.get() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/47-leptos-signals/checks/07-signal-7.rs"]
mod tests;
