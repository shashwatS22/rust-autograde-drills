fn wrap(s: &str) -> Result<i32, String> { s.parse::<i32>().map_err(|e| e.to_string()) }
fn w() -> Result<i32, String> { wrap("2") }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/25-error-design/checks/03-map-err.rs"]
mod tests;
