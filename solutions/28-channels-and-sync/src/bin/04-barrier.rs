use std::sync::{Arc, Barrier};
use std::thread;
fn wait() -> usize { let b = Arc::new(Barrier::new(2)); let b2 = Arc::clone(&b); let h = thread::spawn(move || { b2.wait(); 1 }); b.wait(); h.join().unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/28-channels-and-sync/checks/04-barrier.rs"]
mod tests;
