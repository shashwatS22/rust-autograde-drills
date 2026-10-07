fn consume() -> i32 { vec![1, 2].into_iter().sum() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/42-performance/checks/08-into-iter-owned.rs"]
mod tests;
