struct S<'a> { t: &'a str }
impl<'a> S<'a> { fn get(&self) -> &str { self.t } }
fn g() -> &'static str { S { t: "x" }.get() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/21-lifetimes/checks/06-method.rs"]
mod tests;
