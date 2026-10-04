fn named() -> bool { std::thread::Builder::new().name("t".into()).spawn(|| 1).unwrap().join().unwrap() == 1 }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/27-threads/checks/07-thread-name.rs"]
mod tests;
