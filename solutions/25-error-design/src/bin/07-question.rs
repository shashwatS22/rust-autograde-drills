fn div(a: i32, b: i32) -> Result<i32, &'static str> { if b == 0 { Err("zero") } else { Ok(a / b) } }
fn d() -> Result<i32, &'static str> { div(10, 2) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/25-error-design/checks/07-question.rs"]
mod tests;
