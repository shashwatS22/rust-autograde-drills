use std::sync::Mutex;
fn into_inner() -> i32 {
    let m = Mutex::new(5);
    let guard = m.lock().unwrap();
    *guard + 1
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/38-sync-primitives/checks/07-mutex-poison-recover.rs"]
mod tests;
