fn greet_with(name: &str, greeting: Option<&str>) -> String {
    let g = greeting.unwrap_or("Hello");
    format!("{g}, {name}!")
}
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/08-functions/checks/06-optional-arg.rs"]
mod tests;
