fn largest<T: PartialOrd>(list: &[T]) -> &T { list.iter().max_by(|a, b| a.partial_cmp(b).unwrap()).unwrap() }
fn largest_i32(v: &[i32]) -> i32 { *largest(v) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/17-traits/checks/06-largest.rs"]
mod tests;
