use std::sync::Mutex;
fn m() -> i32 { let g = Mutex::new(4); *g.lock().unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/38-sync-primitives/checks/04-sync-4.rs"]
mod tests;
