fn inc() -> Option<i32> { Some(2).map(|x| x + 1) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/19-generics/checks/10-option-map.rs"]
mod tests;
