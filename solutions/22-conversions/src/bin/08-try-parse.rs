fn bad() -> Result<i32, ()> { "x".parse::<i32>().map_err(|_| ()) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/22-conversions/checks/08-try-parse.rs"]
mod tests;
