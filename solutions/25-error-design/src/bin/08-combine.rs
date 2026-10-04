fn both(a: Result<i32, ()>, b: Result<i32, ()>) -> Result<i32, ()> { a.and_then(|x| b.map(|y| x + y)) }
fn b() -> Result<i32, ()> { both(Ok(1), Ok(2)) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/25-error-design/checks/08-combine.rs"]
mod tests;
