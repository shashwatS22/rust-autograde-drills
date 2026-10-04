struct Meters(u32);
impl From<u32> for Meters { fn from(v: u32) -> Self { Meters(v) } }
fn m() -> u32 { let m: Meters = 5.into(); m.0 }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/22-conversions/checks/02-into.rs"]
mod tests;
