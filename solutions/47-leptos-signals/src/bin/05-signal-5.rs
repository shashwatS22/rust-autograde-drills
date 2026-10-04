use leptos::prelude::*;
fn signal_val() -> i32 { let s = RwSignal::new(5); s.get() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/47-leptos-signals/checks/05-signal-5.rs"]
mod tests;
