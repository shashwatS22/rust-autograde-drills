pub fn parse_one(s: &str) -> Result<i32, ()> { s.parse().map_err(|_| ()) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/26-testing-and-cargo/checks/06-result-ok.rs"]
mod tests;
