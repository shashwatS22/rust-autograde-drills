trait Even { fn is_even(&self) -> bool; }
impl Even for i32 { fn is_even(&self) -> bool { *self % 2 == 0 } }
fn count(v: &[i32]) -> usize { v.iter().filter(|x| x.is_even()).count() }
fn evens() -> usize { count(&[1, 2, 3, 4]) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/20-trait-objects/checks/07-filter-trait.rs"]
mod tests;
