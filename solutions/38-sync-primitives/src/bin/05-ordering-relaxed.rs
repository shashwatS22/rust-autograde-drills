use std::sync::atomic::{AtomicUsize, Ordering};
fn relaxed_inc() -> usize {
    let a = AtomicUsize::new(0);
    a.fetch_add(1, Ordering::Relaxed);
    a.load(Ordering::Relaxed)
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/38-sync-primitives/checks/05-ordering-relaxed.rs"]
mod tests;
