fn evens(v: &[i32]) -> Vec<i32> { v.iter().filter(|x| *x % 2 == 0).copied().collect() }
fn e() -> Vec<i32> { evens(&[1, 2, 3, 4]) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/23-iterators-advanced/checks/03-filter.rs"]
mod tests;
