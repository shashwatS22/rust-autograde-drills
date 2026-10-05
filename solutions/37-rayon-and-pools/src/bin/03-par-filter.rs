use rayon::prelude::*;
fn evens() -> Vec<i32> { (1..=6).into_par_iter().filter(|x| x % 2 == 0).collect() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/37-rayon-and-pools/checks/03-par-filter.rs"]
mod tests;
