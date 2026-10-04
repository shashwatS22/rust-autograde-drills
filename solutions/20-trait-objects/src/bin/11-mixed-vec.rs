fn mix() -> usize { let v: Vec<Box<dyn std::fmt::Debug>> = vec![Box::new(1i32), Box::new("a")]; v.len() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/20-trait-objects/checks/11-mixed-vec.rs"]
mod tests;
