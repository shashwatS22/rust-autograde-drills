fn doubled() -> Vec<i32> { vec![1, 2].into_iter().map(|x| x * 2).collect() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/19-generics/checks/09-collect.rs"]
mod tests;
