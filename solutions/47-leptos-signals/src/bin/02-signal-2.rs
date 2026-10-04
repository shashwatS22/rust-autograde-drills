use leptos::prelude::*;
fn signal_val() -> i32 { let s = RwSignal::new(2); s.get() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/47-leptos-signals/checks/02-signal-2.rs"]
mod tests;
