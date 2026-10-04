fn show() -> String {
    #[derive(Debug)]
    enum C { Red }
    format!("{:?}", C::Red)
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/18-derive-and-operators/checks/01-derive-debug.rs"]
mod tests;
