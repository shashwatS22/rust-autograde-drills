fn ok() -> Result<i32, ()> { Ok(3).map(|x| x + 1) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/19-generics/checks/11-result-map.rs"]
mod tests;
