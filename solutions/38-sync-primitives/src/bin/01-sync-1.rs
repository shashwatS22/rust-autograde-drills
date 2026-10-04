use std::sync::Mutex;
fn m() -> i32 { let g = Mutex::new(1); *g.lock().unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/38-sync-primitives/checks/01-sync-1.rs"]
mod tests;
