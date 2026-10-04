struct Wrapper(i32);
impl From<i32> for Wrapper { fn from(v: i32) -> Self { Wrapper(v) } }
fn wrap() -> i32 { Wrapper::from(3).0 }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/22-conversions/checks/01-from-into.rs"]
mod tests;
