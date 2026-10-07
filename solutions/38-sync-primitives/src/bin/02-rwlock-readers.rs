use std::sync::RwLock;
fn many_reads() -> i32 {
    let lock = RwLock::new(4);
    let r1 = lock.read().unwrap();
    let r2 = lock.read().unwrap();
    *r1 + *r2
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/38-sync-primitives/checks/02-rwlock-readers.rs"]
mod tests;
