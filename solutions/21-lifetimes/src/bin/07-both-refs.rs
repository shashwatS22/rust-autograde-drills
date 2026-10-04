fn both<'a>(a: &'a str, b: &'a str) -> (&'a str, &'a str) { (a, b) }
fn p() -> (&'static str, &'static str) { both("a", "b") }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/21-lifetimes/checks/07-both-refs.rs"]
mod tests;
