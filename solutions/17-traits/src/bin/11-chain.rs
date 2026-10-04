trait Twice { fn double(self) -> i32; }
impl Twice for i32 { fn double(self) -> i32 { self * 2 } }
fn twice_five() -> i32 { 5.double() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/17-traits/checks/11-chain.rs"]
mod tests;
