use std::sync::{Arc, Mutex, Condvar};
fn signal() -> i32 { let pair = Arc::new((Mutex::new(false), Condvar::new())); let (lock, cv) = &*pair; let mut started = lock.lock().unwrap(); *started = true; cv.notify_one(); 1 }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/28-channels-and-sync/checks/03-condvar.rs"]
mod tests;
