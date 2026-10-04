use std::sync::Mutex;
fn m() -> i32 { let g = Mutex::new(5); *g.lock().unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/38-sync-primitives/checks/05-sync-5.rs"]
mod tests;
