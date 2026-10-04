use leptos::prelude::*;
fn signal_val() -> i32 { let s = RwSignal::new(11); s.get() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/47-leptos-signals/checks/11-signal-11.rs"]
mod tests;
