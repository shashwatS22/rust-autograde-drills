fn sync() -> i32 { tokio::runtime::Runtime::new().unwrap().block_on(async { 3 }) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/29-async-tokio/checks/07-block-on.rs"]
mod tests;
