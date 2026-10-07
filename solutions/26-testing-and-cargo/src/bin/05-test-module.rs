mod math { pub fn sq(x: i32) -> i32 { x * x } }
pub fn sq() -> i32 { math::sq(3) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/26-testing-and-cargo/checks/05-test-module.rs"]
mod tests;
