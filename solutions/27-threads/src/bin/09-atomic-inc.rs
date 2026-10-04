use std::sync::atomic::{AtomicUsize, Ordering};
fn inc() -> usize { let a = AtomicUsize::new(0); a.fetch_add(1, Ordering::SeqCst); a.load(Ordering::SeqCst) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/27-threads/checks/09-atomic-inc.rs"]
mod tests;
