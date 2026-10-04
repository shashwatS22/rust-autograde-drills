trait Equals { fn eq(&self, other: &Self) -> bool; }
impl Equals for i32 { fn eq(&self, other: &Self) -> bool { self == other } }
fn same(a: i32, b: i32) -> bool { Equals::eq(&a, &b) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/17-traits/checks/08-partial-eq-trait.rs"]
mod tests;
