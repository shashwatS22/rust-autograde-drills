fn first<T: Copy>(v: &[T]) -> Option<T> { v.first().copied() }
fn got() -> i32 { first(&[9, 1]).unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/19-generics/checks/07-first.rs"]
mod tests;
