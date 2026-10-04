fn head(s: &str) -> &str { &s[..2] }
fn h() -> &'static str { head("rust") }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/21-lifetimes/checks/10-slice.rs"]
mod tests;
