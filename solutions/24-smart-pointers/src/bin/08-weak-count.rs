use std::rc::{Rc, Weak};
fn weak() -> bool { let r = Rc::new(1); let w: Weak<_> = Rc::downgrade(&r); w.upgrade().is_some() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/24-smart-pointers/checks/08-weak-count.rs"]
mod tests;
