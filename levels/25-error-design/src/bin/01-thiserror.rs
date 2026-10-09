//! 25-error-design / 01-thiserror
//!
//! TASK
//! Define `AppError` with thiserror.
//!
//! CONCEPT
//! thiserror derives Error with Display and source for enum variants with fields.
//!
//! SIGNATURE
//! fn parse_port(s: &str) -> Result<u16, AppError>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use thiserror::Error;
#[derive(Debug, Error)]
enum AppError { #[error("bad port")] BadPort }
fn parse_port(s: &str) -> Result<u16, AppError> { s.parse().map_err(|_| AppError::BadPort) }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-thiserror.rs"]
mod tests;