fn box_size() -> usize { std::mem::size_of::<Box<i32>>() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/39-memory-layout/checks/05-box-size.rs"]
mod tests;
