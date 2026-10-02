fn power(base: u64, exp: u32) -> u64 { if exp == 0 { 1 } else { base * power(base, exp - 1) } }
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/14-recursion/checks/09-power.rs"]
mod tests;
