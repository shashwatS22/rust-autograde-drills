fn from() -> Result<(), std::num::ParseIntError> { "1".parse::<i32>().map(|_| ()) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/25-error-design/checks/10-from-err.rs"]
mod tests;
