fn idx() -> usize { ["a", "b"].iter().enumerate().find(|(i, _)| *i == 1).map(|(_, s)| s.len()).unwrap_or(0) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/23-iterators-advanced/checks/09-enumerate.rs"]
mod tests;
