fn parse() -> Result<i32, std::num::TryFromIntError> { i32::try_from(42i64) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/22-conversions/checks/03-try-from.rs"]
mod tests;
