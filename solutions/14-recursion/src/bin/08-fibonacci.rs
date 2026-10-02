fn fib(n: u32) -> u64 { if n == 0 { 0 } else if n == 1 { 1 } else { fib(n - 1) + fib(n - 2) } }
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/14-recursion/checks/08-fibonacci.rs"]
mod tests;
