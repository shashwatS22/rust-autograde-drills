fn count<T>(v: &[T]) -> usize { v.len() }
fn three() -> usize { count(&[1, 2, 3]) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/19-generics/checks/06-count.rs"]
mod tests;
