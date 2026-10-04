fn zip_sum() -> i32 { [1, 2].iter().zip([10, 20].iter()).map(|(a, b)| a + b).sum() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/23-iterators-advanced/checks/08-zip.rs"]
mod tests;
