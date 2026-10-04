use std::sync::Mutex;
fn m() -> i32 { let g = Mutex::new(9); *g.lock().unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/38-sync-primitives/checks/09-sync-9.rs"]
mod tests;
