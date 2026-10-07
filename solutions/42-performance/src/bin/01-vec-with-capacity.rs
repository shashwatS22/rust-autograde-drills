fn cap_len() -> usize { let v: Vec<i32> = Vec::with_capacity(100); v.capacity() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/42-performance/checks/01-vec-with-capacity.rs"]
mod tests;
