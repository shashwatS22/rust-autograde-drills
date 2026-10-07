use leptos::prelude::*;
fn sum() -> i32 { let a = RwSignal::new(1); let b = RwSignal::new(2); let m = Memo::new(move |_| a.get() + b.get()); m.get() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/47-leptos-signals/checks/08-memo-sum.rs"]
mod tests;
