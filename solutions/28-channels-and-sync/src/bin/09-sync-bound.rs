fn is_sync<T: Sync>() -> bool { true }
fn s() -> bool { is_sync::<i32>() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/28-channels-and-sync/checks/09-sync-bound.rs"]
mod tests;
