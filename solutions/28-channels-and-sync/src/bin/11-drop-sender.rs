use std::sync::mpsc;
fn closed() -> bool { let (tx, rx) = mpsc::channel::<i32>(); drop(tx); rx.recv().is_err() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/28-channels-and-sync/checks/11-drop-sender.rs"]
mod tests;
