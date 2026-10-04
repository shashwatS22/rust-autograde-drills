fn cloned() -> i32 {
    #[derive(Clone, Copy)]
    struct P { v: i32 }
    let a = P { v: 3 };
    a.clone().v
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/18-derive-and-operators/checks/02-derive-clone.rs"]
mod tests;
