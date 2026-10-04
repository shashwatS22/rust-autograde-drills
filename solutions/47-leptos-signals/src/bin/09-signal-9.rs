use leptos::prelude::*;
fn signal_val() -> i32 { let s = RwSignal::new(9); s.get() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/47-leptos-signals/checks/09-signal-9.rs"]
mod tests;
