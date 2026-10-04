use std::sync::Mutex;
fn tryl() -> bool { let m = Mutex::new(1); m.try_lock().is_ok() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/28-channels-and-sync/checks/07-try-lock.rs"]
mod tests;
