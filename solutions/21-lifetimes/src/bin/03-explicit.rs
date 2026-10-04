fn identity<'a>(x: &'a str) -> &'a str { x }
fn id() -> &'static str { identity("ok") }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/21-lifetimes/checks/03-explicit.rs"]
mod tests;
