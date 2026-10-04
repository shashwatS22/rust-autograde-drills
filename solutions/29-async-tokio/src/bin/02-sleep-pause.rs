async fn delayed() -> i32 { tokio::time::sleep(std::time::Duration::from_secs(60)).await; 1 }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/29-async-tokio/checks/02-sleep-pause.rs"]
mod tests;
