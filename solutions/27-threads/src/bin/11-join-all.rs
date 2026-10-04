use std::thread;
fn total() -> i32 { let hs = vec![thread::spawn(|| 1), thread::spawn(|| 2)]; hs.into_iter().map(|h| h.join().unwrap()).sum() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/27-threads/checks/11-join-all.rs"]
mod tests;
