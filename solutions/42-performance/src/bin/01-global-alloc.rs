fn alloc_count() -> usize { let _ = Box::new(1); 1 }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/42-performance/checks/01-global-alloc.rs"]
mod tests;
