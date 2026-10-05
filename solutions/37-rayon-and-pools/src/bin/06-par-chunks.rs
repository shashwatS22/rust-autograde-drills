use rayon::prelude::*;
fn chunk_sum() -> i32 { [1, 2, 3, 4].par_chunks(2).map(|c| c.iter().sum::<i32>()).sum() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/37-rayon-and-pools/checks/06-par-chunks.rs"]
mod tests;
