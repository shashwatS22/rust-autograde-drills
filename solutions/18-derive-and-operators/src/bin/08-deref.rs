use std::ops::Deref;
fn len() -> usize {
    struct S(String);
    impl Deref for S { type Target = str; fn deref(&self) -> &str { &self.0 } }
    S("abc".into()).len()
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/18-derive-and-operators/checks/08-deref.rs"]
mod tests;
