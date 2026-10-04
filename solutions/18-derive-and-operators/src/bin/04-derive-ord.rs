fn sorted() -> Vec<i32> {
    #[derive(Ord, PartialOrd, Eq, PartialEq, Clone)]
    struct S { v: i32 }
    let mut v = vec![S { v: 2 }, S { v: 1 }];
    v.sort();
    v.into_iter().map(|s| s.v).collect()
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/18-derive-and-operators/checks/04-derive-ord.rs"]
mod tests;
