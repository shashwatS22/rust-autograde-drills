use std::borrow::Cow;
fn cow() -> usize { Cow::from("hi").len() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/24-smart-pointers/checks/07-cow.rs"]
mod tests;
