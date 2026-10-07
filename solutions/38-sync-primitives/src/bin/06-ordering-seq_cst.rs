use std::sync::atomic::{AtomicBool, Ordering};
fn flag_seen() -> bool {
    let flag = AtomicBool::new(false);
    flag.store(true, Ordering::SeqCst);
    flag.load(Ordering::SeqCst)
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/38-sync-primitives/checks/06-ordering-seq_cst.rs"]
mod tests;
