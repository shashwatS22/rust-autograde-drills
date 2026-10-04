use std::collections::HashSet;
fn uniq() -> usize {
    let s: HashSet<i32> = [1, 1, 2].into_iter().collect();
    s.len()
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/18-derive-and-operators/checks/11-hash-set.rs"]
mod tests;
