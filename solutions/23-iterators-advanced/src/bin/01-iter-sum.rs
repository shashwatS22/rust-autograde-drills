fn sum(v: &[i32]) -> i32 { v.iter().sum() }
fn ten() -> i32 { sum(&[1, 2, 3, 4]) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/23-iterators-advanced/checks/01-iter-sum.rs"]
mod tests;
