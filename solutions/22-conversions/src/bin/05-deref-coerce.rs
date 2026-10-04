use std::ops::Deref;
struct S(String);
impl Deref for S { type Target = str; fn deref(&self) -> &str { &self.0 } }
fn upper(s: &str) -> String { s.to_uppercase() }
fn u() -> String { upper(&S("hi".into())) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/22-conversions/checks/05-deref-coerce.rs"]
mod tests;
