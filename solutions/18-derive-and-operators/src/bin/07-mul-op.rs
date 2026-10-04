use std::ops::Mul;
fn triple() -> i32 {
    struct W(i32);
    impl Mul<i32> for W { type Output = i32; fn mul(self, rhs: i32) -> i32 { self.0 * rhs } }
    W(3) * 2
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/18-derive-and-operators/checks/07-mul-op.rs"]
mod tests;
