use leptos::prelude::*;
fn signal_val() -> i32 { let s = RwSignal::new(10); s.get() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/47-leptos-signals/checks/10-signal-10.rs"]
mod tests;
