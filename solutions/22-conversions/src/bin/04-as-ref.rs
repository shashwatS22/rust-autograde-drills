fn len(s: impl AsRef<str>) -> usize { s.as_ref().len() }
fn l() -> usize { len("abc") }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/22-conversions/checks/04-as-ref.rs"]
mod tests;
