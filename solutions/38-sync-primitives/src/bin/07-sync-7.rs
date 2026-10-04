use std::sync::Mutex;
fn m() -> i32 { let g = Mutex::new(7); *g.lock().unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/38-sync-primitives/checks/07-sync-7.rs"]
mod tests;
