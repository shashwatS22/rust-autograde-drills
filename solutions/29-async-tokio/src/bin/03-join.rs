async fn both() -> (i32, i32) { tokio::join!(async { 1 }, async { 2 }) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/29-async-tokio/checks/03-join.rs"]
mod tests;
