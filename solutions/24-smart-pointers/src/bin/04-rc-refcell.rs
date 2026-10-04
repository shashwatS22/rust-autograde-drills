use std::rc::Rc;
use std::cell::RefCell;
fn combo() -> i32 { let v = Rc::new(RefCell::new(2)); *v.borrow() * 2 }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/24-smart-pointers/checks/04-rc-refcell.rs"]
mod tests;
