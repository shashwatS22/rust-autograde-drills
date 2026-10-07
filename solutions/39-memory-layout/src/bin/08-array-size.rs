fn arr() -> usize { std::mem::size_of::<[u8; 16]>() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/39-memory-layout/checks/08-array-size.rs"]
mod tests;
