use rayon::prelude::*;
fn sorted() -> Vec<i32> { let mut v: Vec<i32> = (0..5).rev().collect(); v.par_sort(); v }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/37-rayon-and-pools/checks/05-par-sort.rs"]
mod tests;
