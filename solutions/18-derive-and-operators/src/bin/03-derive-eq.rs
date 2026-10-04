fn eq_ok() -> bool {
    #[derive(PartialEq)]
    struct P { v: i32 }
    P { v: 1 } == P { v: 1 }
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/18-derive-and-operators/checks/03-derive-eq.rs"]
mod tests;
