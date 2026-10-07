use std::sync::{Arc, Condvar, Mutex};
use std::thread;
fn worker_wakes() -> i32 {
    let pair = Arc::new((Mutex::new(0i32), Condvar::new()));
    let pair2 = Arc::clone(&pair);
    let h = thread::spawn(move || {
        let (lock, cv) = &*pair2;
        let mut v = lock.lock().unwrap();
        *v = 7;
        cv.notify_one();
    });
    let (lock, cv) = &*pair;
    let mut v = lock.lock().unwrap();
    while *v == 0 { v = cv.wait(v).unwrap(); }
    h.join().unwrap();
    *v
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/38-sync-primitives/checks/04-condvar-pair.rs"]
mod tests;
