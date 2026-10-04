use std::sync::Mutex;
fn m() -> i32 { let g = Mutex::new(2); *g.lock().unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/38-sync-primitives/checks/02-sync-2.rs"]
mod tests;
