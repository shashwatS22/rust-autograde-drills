//! 35-sqlx / 08-max-value
//!
//! TASK
//! Return the maximum value in a column via SQL.
//!
//! SIGNATURE
//! async fn max_val() -> Result<i32, sqlx::Error>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use sqlx::SqlitePool;
async fn max_val() -> Result<i32, sqlx::Error> { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-max-value.rs"]
mod tests;
