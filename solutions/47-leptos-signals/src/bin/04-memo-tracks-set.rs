use leptos::prelude::*;
fn after_change() -> i32 { let n = RwSignal::new(1); let d = Memo::new(move |_| n.get() + 10); n.set(2); d.get() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/47-leptos-signals/checks/04-memo-tracks-set.rs"]
mod tests;
