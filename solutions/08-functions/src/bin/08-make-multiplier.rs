fn make_multiplier(n: i32) -> impl Fn(i32) -> i32 { move |x| x * n }
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/08-functions/checks/08-make-multiplier.rs"]
mod tests;
