use rayon::prelude::*;
fn par_len() -> usize { (0..100).into_par_iter().count() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/37-rayon-and-pools/checks/08-par-len.rs"]
mod tests;
