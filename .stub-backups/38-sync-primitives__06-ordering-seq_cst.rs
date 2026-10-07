//! 38-sync-primitives / 06-ordering-seq_cst
//!
//! TASK
//! Publish a flag with `SeqCst` store/load.
//!
//! SIGNATURE
//! fn flag_seen() -> bool
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::sync::atomic::{AtomicBool, Ordering};
fn flag_seen() -> bool {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/06-ordering-seq_cst.rs"]
mod tests;
