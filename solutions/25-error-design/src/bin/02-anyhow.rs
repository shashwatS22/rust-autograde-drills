fn read_num(s: &str) -> anyhow::Result<i32> { Ok(s.parse()?)}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/25-error-design/checks/02-anyhow.rs"]
mod tests;
