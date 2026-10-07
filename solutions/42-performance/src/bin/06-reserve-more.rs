fn reserved() -> usize { let mut v = vec![1, 2]; v.reserve(10); v.capacity() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/42-performance/checks/06-reserve-more.rs"]
mod tests;
