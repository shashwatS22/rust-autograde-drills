fn chain() -> Vec<i32> { [1].iter().chain([2].iter()).copied().collect() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/23-iterators-advanced/checks/07-chain.rs"]
mod tests;
