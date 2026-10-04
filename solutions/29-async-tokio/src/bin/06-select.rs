async fn pick() -> i32 { tokio::select! { v = async { 1 } => v, } }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/29-async-tokio/checks/06-select.rs"]
mod tests;
