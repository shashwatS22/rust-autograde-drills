use std::sync::Mutex;
fn m() -> i32 { let g = Mutex::new(10); *g.lock().unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/38-sync-primitives/checks/10-sync-10.rs"]
mod tests;
