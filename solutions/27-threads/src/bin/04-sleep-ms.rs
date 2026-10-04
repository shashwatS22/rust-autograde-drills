use std::thread;
use std::time::Duration;
fn ok() -> bool { thread::sleep(Duration::from_millis(1)); true }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/27-threads/checks/04-sleep-ms.rs"]
mod tests;
