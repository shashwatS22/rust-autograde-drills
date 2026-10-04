fn find(v: &[i32]) -> Option<i32> { v.iter().copied().find(|x| *x > 2) }
fn g() -> Option<i32> { find(&[1, 3, 2]) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/23-iterators-advanced/checks/05-find.rs"]
mod tests;
