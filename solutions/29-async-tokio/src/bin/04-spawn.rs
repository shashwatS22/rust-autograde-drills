async fn spawned() -> i32 { let h = tokio::spawn(async { 4 }); h.await.unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/29-async-tokio/checks/04-spawn.rs"]
mod tests;
