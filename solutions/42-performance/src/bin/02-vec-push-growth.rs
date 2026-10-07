fn after_push() -> usize { let mut v = Vec::new(); v.push(1); v.push(2); v.len() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/42-performance/checks/02-vec-push-growth.rs"]
mod tests;
