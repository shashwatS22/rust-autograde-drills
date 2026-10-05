//! 35-sqlx / 03-sum-column
//!
//! TASK
//! Store integers in `nums` and return their SQL `SUM`.
//!
//! SIGNATURE
//! async fn sum_nums() -> Result<i64, sqlx::Error>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use sqlx::SqlitePool;
async fn sum_nums() -> Result<i64, sqlx::Error> { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/03-sum-column.rs"]
mod tests;
