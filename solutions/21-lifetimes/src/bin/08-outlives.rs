fn choose<'a>(flag: bool, a: &'a str, b: &'a str) -> &'a str { if flag { a } else { b } }
fn c() -> &'static str { choose(true, "y", "n") }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/21-lifetimes/checks/08-outlives.rs"]
mod tests;
