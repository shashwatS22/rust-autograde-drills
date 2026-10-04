fn is_send<T: Send>() -> bool { true }
fn s() -> bool { is_send::<i32>() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/28-channels-and-sync/checks/08-send-sync.rs"]
mod tests;
