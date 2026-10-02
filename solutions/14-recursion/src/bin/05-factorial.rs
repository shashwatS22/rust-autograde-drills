fn factorial(n: u64) -> u64 { if n == 0 { 1 } else { n * factorial(n - 1) } }
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/14-recursion/checks/05-factorial.rs"]
mod tests;
