fn align_u32() -> usize { std::mem::align_of::<u32>() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/39-memory-layout/checks/02-align-of.rs"]
mod tests;
