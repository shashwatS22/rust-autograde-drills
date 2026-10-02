fn sum_digits(n: u64) -> u64 { if n == 0 { 0 } else { (n % 10) + sum_digits(n / 10) } }
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/14-recursion/checks/10-sum-digits.rs"]
mod tests;
