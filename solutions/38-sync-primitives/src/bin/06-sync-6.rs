use std::sync::Mutex;
fn m() -> i32 { let g = Mutex::new(6); *g.lock().unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/38-sync-primitives/checks/06-sync-6.rs"]
mod tests;
