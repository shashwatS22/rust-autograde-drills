fn age() -> u32 {
    #[derive(Default)]
    struct P { age: u32 }
    P::default().age
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/18-derive-and-operators/checks/10-default.rs"]
mod tests;
