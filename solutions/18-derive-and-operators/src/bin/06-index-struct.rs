use std::ops::Index;
fn second() -> i32 {
    struct Pair(i32, i32);
    impl Index<usize> for Pair { type Output = i32; fn index(&self, i: usize) -> &i32 { if i == 0 { &self.0 } else { &self.1 } } }
    Pair(1, 9)[1]
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/18-derive-and-operators/checks/06-index-struct.rs"]
mod tests;
