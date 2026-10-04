use std::rc::Rc;
fn shared() -> i32 { let a = Rc::new(3); let b = Rc::clone(&a); *a + *b }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/24-smart-pointers/checks/02-rc-share.rs"]
mod tests;
