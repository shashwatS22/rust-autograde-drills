fn boxed() -> i32 { let b = Box::new(5); *b }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/24-smart-pointers/checks/01-box-heap.rs"]
mod tests;
