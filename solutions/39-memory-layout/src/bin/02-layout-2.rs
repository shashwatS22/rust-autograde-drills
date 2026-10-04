fn size() -> usize { std::mem::size_of::<i32>() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/39-memory-layout/checks/02-layout-2.rs"]
mod tests;
