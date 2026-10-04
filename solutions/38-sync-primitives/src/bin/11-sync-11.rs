use std::sync::Mutex;
fn m() -> i32 { let g = Mutex::new(11); *g.lock().unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/38-sync-primitives/checks/11-sync-11.rs"]
mod tests;
