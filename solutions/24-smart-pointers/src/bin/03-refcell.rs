use std::cell::RefCell;
fn mutate() -> i32 { let c = RefCell::new(1); *c.borrow_mut() += 2; *c.borrow() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/24-smart-pointers/checks/03-refcell.rs"]
mod tests;
