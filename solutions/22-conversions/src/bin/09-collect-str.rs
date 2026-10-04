fn joined() -> String { ["a", "b"].iter().cloned().collect::<String>() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/22-conversions/checks/09-collect-str.rs"]
mod tests;
