use rayon::prelude::*;
fn doubled() -> Vec<i32> { (1..4).into_par_iter().map(|x| x * 2).collect() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/37-rayon-and-pools/checks/02-par-map.rs"]
mod tests;
