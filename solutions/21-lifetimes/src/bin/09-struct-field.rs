struct Holder { value: i32 }
fn get() -> i32 { Holder { value: 5 }.value }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/21-lifetimes/checks/09-struct-field.rs"]
mod tests;
