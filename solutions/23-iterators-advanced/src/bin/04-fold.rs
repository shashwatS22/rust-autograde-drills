fn fold_sum(v: &[i32]) -> i32 { v.iter().fold(0, |a, b| a + *b) }
fn f() -> i32 { fold_sum(&[1, 2, 3]) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/23-iterators-advanced/checks/04-fold.rs"]
mod tests;
