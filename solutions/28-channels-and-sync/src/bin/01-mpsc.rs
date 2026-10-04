use std::sync::mpsc;
fn send_recv() -> i32 { let (tx, rx) = mpsc::channel(); tx.send(5).unwrap(); rx.recv().unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/28-channels-and-sync/checks/01-mpsc.rs"]
mod tests;
