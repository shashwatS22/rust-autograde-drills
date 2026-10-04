use thiserror::Error;
#[derive(Debug, Error)]
enum AppError { #[error("bad port")] BadPort }
fn parse_port(s: &str) -> Result<u16, AppError> { s.parse().map_err(|_| AppError::BadPort) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/25-error-design/checks/01-thiserror.rs"]
mod tests;
