fn clone_count_hint() -> usize { let a = String::from("hi"); let b = a.clone(); a.len() + b.len() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/42-performance/checks/03-string-clone-allocs.rs"]
mod tests;
