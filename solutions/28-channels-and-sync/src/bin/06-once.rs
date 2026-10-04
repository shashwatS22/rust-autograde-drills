use std::sync::OnceLock;
fn once() -> &'static str { static O: OnceLock<String> = OnceLock::new(); O.get_or_init(|| "ok".into()) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/28-channels-and-sync/checks/06-once.rs"]
mod tests;
