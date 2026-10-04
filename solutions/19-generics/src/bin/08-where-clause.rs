fn clamp(v: i32, lo: i32, hi: i32) -> i32 { v.clamp(lo, hi) }
fn small() -> i32 { clamp(10, 0, 5) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/19-generics/checks/08-where-clause.rs"]
mod tests;
