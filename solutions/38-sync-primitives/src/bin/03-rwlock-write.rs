use std::sync::RwLock;
fn write_bump() -> i32 {
    let lock = RwLock::new(1);
    { *lock.write().unwrap() += 2; }
    *lock.read().unwrap()
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/38-sync-primitives/checks/03-rwlock-write.rs"]
mod tests;
