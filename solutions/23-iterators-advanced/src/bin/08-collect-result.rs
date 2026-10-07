fn parse_all(v: &[&str]) -> Result<Vec<i32>, std::num::ParseIntError> { v.iter().map(|s| s.parse()).collect() }
fn ok() -> Result<Vec<i32>, std::num::ParseIntError> { parse_all(&["1", "2"]) }
fn bad() -> Result<Vec<i32>, std::num::ParseIntError> { parse_all(&["1", "x"]) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/23-iterators-advanced/checks/08-collect-result.rs"]
mod tests;
