fn ids() -> usize { std::thread::available_parallelism().map(|n| n.get()).unwrap_or(1).max(1) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/27-threads/checks/05-yield.rs"]
mod tests;
