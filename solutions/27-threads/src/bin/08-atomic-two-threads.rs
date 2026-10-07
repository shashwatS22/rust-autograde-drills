use std::sync::atomic::{AtomicUsize, Ordering};
use std::sync::Arc;
use std::thread;
fn two_thread_inc() -> usize {
    let c = Arc::new(AtomicUsize::new(0));
    let a = Arc::clone(&c);
    let b = Arc::clone(&c);
    let h1 = thread::spawn(move || { a.fetch_add(1, Ordering::SeqCst); });
    let h2 = thread::spawn(move || { b.fetch_add(1, Ordering::SeqCst); });
    h1.join().unwrap();
    h2.join().unwrap();
    c.load(Ordering::SeqCst)
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/27-threads/checks/08-atomic-two-threads.rs"]
mod tests;
