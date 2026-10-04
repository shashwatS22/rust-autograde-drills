fn swap<T>(a: T, b: T) -> (T, T) { (b, a) }
fn swapped() -> (i32, i32) { swap(1, 2) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/19-generics/checks/05-swap.rs"]
mod tests;
