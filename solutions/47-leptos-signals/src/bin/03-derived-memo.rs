use leptos::prelude::*;
fn doubled() -> i32 { let n = RwSignal::new(4); let d = Memo::new(move |_| n.get() * 2); d.get() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/47-leptos-signals/checks/03-derived-memo.rs"]
mod tests;
