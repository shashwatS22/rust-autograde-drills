async fn chan() -> i32 { let (tx, mut rx) = tokio::sync::mpsc::channel(1); tx.send(9).await.unwrap(); rx.recv().await.unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/29-async-tokio/checks/08-channel.rs"]
mod tests;
