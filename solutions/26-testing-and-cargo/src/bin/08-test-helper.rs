pub fn greet(name: &str) -> String { format!("Hello, {name}!") }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/26-testing-and-cargo/checks/08-test-helper.rs"]
mod tests;
