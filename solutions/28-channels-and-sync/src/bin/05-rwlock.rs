use std::sync::RwLock;
fn read() -> i32 { let l = RwLock::new(3); *l.read().unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/28-channels-and-sync/checks/05-rwlock.rs"]
mod tests;
