fn extend_len() -> usize { let mut v = vec![1]; v.extend([2, 3]); v.len() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/42-performance/checks/05-extend-vs-push.rs"]
mod tests;
