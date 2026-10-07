use std::sync::Arc;
use std::thread;
fn arc_value() -> i32 {
    let v = Arc::new(42i32);
    let c = Arc::clone(&v);
    let h = thread::spawn(move || *c);
    h.join().unwrap()
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/28-channels-and-sync/checks/08-arc-cross-thread.rs"]
mod tests;
