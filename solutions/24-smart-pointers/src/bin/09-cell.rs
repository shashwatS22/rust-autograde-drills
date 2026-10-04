use std::cell::Cell;
fn cell() -> i32 { let c = Cell::new(1); c.set(4); c.get() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/24-smart-pointers/checks/09-cell.rs"]
mod tests;
