struct Pair<T>(pub T, pub T);
fn first() -> i32 { Pair(7, 8).0 }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/19-generics/checks/03-pair.rs"]
mod tests;
