use std::thread;
fn doubled() -> i32 { let h = thread::spawn(|| 21); h.join().unwrap() * 2 }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/27-threads/checks/01-spawn-join.rs"]
mod tests;
