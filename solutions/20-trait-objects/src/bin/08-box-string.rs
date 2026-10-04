fn boxed_str() -> String { (*Box::new("rust".to_string())).clone() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/20-trait-objects/checks/08-box-string.rs"]
mod tests;
