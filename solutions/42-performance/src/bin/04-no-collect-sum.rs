fn sum_iter() -> i32 { (0..5).map(|x| x).sum() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/42-performance/checks/04-no-collect-sum.rs"]
mod tests;
