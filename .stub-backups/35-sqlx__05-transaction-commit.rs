//! 35-sqlx / 05-transaction-commit
//!
//! TASK
//! Use a transaction to insert two rows; both must be visible after commit.
//!
//! SIGNATURE
//! async fn tx_count() -> Result<i64, sqlx::Error>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use sqlx::SqlitePool;
async fn tx_count() -> Result<i64, sqlx::Error> { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/05-transaction-commit.rs"]
mod tests;