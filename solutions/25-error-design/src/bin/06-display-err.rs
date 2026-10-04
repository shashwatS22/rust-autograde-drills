use thiserror::Error;
#[derive(Error, Debug)]
#[error("code {0}")]
struct E(u32);
fn msg() -> String { E(5).to_string() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/25-error-design/checks/06-display-err.rs"]
mod tests;
