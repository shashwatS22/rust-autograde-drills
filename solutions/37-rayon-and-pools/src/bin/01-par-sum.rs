use rayon::prelude::*;
fn par_sum() -> i32 { (0..10).into_par_iter().sum() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/37-rayon-and-pools/checks/01-par-sum.rs"]
mod tests;
