use std::sync::atomic::{AtomicUsize, Ordering};
use std::sync::Arc;
use std::thread;
fn parallel_add() -> usize {
    let n = Arc::new(AtomicUsize::new(0));
    let a = Arc::clone(&n);
    let b = Arc::clone(&n);
    let h1 = thread::spawn(move || { a.fetch_add(10, Ordering::SeqCst); });
    let h2 = thread::spawn(move || { b.fetch_add(5, Ordering::SeqCst); });
    h1.join().unwrap(); h2.join().unwrap();
    n.load(Ordering::SeqCst)
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/38-sync-primitives/checks/01-atomic-fetch-two.rs"]
mod tests;
