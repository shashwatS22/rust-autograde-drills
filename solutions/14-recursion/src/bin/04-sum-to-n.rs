fn sum_to(n: u32) -> u32 { if n == 0 { 0 } else { n + sum_to(n - 1) } }
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/14-recursion/checks/04-sum-to-n.rs"]
mod tests;
