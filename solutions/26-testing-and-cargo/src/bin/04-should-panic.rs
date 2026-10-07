pub fn divide(a: i32, b: i32) -> i32 { if b == 0 { panic!("zero"); } a / b }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/26-testing-and-cargo/checks/04-should-panic.rs"]
mod tests;
