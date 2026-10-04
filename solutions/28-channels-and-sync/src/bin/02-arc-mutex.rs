use std::sync::{Arc, Mutex};
use std::thread;
fn shared() -> i32 { let m = Arc::new(Mutex::new(0)); let mut h = vec![]; for _ in 0..2 { let c = Arc::clone(&m); h.push(thread::spawn(move || { *c.lock().unwrap() += 1; })); } for j in h { j.join().unwrap(); } *m.lock().unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/28-channels-and-sync/checks/02-arc-mutex.rs"]
mod tests;
