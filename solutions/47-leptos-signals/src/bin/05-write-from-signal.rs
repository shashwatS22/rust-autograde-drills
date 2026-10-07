use leptos::prelude::*;
fn synced() -> i32 { let a = RwSignal::new(3); let b = RwSignal::new(0); b.set(a.get()); a.set(9); b.get() + a.get() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/47-leptos-signals/checks/05-write-from-signal.rs"]
mod tests;
