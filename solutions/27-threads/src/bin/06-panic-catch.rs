fn caught() -> bool { std::panic::catch_unwind(|| panic!("x")).is_err() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/27-threads/checks/06-panic-catch.rs"]
mod tests;
