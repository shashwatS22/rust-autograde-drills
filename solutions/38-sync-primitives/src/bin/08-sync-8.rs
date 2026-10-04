use std::sync::Mutex;
fn m() -> i32 { let g = Mutex::new(8); *g.lock().unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/38-sync-primitives/checks/08-sync-8.rs"]
mod tests;
