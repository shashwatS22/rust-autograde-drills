struct Config { retries: u32, timeout_ms: u32 }
impl Default for Config {
    fn default() -> Self { Self { retries: 3, timeout_ms: 1000 } }
}
fn default_retries() -> u32 { Config::default().retries }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/18-derive-and-operators/checks/07-default-override.rs"]
mod tests;
