//! 37-rayon-and-pools / 01-par-sum
//!
//! TASK
//! Sum 0..10 with `into_par_iter()`.
//!
//! CONCEPT
//! rayon par_iter splits work across a thread pool for CPU-bound loops.
//!
//! SIGNATURE
//! fn par_sum() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use rayon::prelude::*;
fn par_sum() -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-par-sum.rs"]
mod tests;