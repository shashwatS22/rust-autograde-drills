fn drain_sum() -> i32 { let mut v = vec![1, 2, 3]; v.drain(..).sum() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/42-performance/checks/07-drain-reuse.rs"]
mod tests;
