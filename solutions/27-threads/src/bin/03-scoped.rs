fn sum() -> i32 { std::thread::scope(|s| { let h = s.spawn(|| 3); h.join().unwrap() }) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/27-threads/checks/03-scoped.rs"]
mod tests;
