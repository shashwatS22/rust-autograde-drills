use std::thread;
fn moved() -> i32 { let v = vec![1, 2]; let h = thread::spawn(move || v.len()); h.join().unwrap() as i32 }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/27-threads/checks/02-move-closure.rs"]
mod tests;
