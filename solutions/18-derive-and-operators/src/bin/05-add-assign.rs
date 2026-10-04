use std::ops::AddAssign;
fn bump() -> i32 {
    struct C { n: i32 }
    impl AddAssign for C { fn add_assign(&mut self, rhs: Self) { self.n += rhs.n } }
    let mut c = C { n: 1 };
    c += C { n: 2 };
    c.n
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/18-derive-and-operators/checks/05-add-assign.rs"]
mod tests;
