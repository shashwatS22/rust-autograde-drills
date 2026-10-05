use rayon::prelude::*;
fn par_product() -> i32 { [1, 2, 3, 4].par_iter().copied().reduce(|| 1, |a, b| a * b) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/37-rayon-and-pools/checks/04-par-fold.rs"]
mod tests;
