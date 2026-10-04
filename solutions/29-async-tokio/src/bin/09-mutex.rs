async fn lock() -> i32 { let m = tokio::sync::Mutex::new(5); *m.lock().await }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/29-async-tokio/checks/09-mutex.rs"]
mod tests;
