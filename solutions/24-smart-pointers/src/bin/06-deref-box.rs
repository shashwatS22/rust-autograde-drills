use std::ops::Deref;
fn len() -> usize { Box::new("abc".to_string()).len() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/24-smart-pointers/checks/06-deref-box.rs"]
mod tests;
