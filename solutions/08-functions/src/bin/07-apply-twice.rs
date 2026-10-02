fn apply_twice(f: impl Fn(i32) -> i32, value: i32) -> i32 { f(f(value)) }
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/08-functions/checks/07-apply-twice.rs"]
mod tests;
