fn greet(name: &str) -> String { format!("Hello, {name}!") }
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/08-functions/checks/05-greet.rs"]
mod tests;
