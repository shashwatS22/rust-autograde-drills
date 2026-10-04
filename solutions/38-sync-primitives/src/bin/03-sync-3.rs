use std::sync::Mutex;
fn m() -> i32 { let g = Mutex::new(3); *g.lock().unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/38-sync-primitives/checks/03-sync-3.rs"]
mod tests;
