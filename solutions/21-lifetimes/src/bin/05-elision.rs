fn first(s: &str) -> &str { &s[0..1] }
fn f() -> &'static str { first("abc") }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/21-lifetimes/checks/05-elision.rs"]
mod tests;
