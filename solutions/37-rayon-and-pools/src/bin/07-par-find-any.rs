use rayon::prelude::*;
fn has_seven() -> bool { (1..=10).into_par_iter().any(|x| x == 7) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/37-rayon-and-pools/checks/07-par-find-any.rs"]
mod tests;
