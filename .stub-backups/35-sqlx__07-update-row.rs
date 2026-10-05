//! 35-sqlx / 07-update-row
//!
//! TASK
//! Update a column value and read it back.
//!
//! SIGNATURE
//! async fn updated() -> Result<i32, sqlx::Error>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use sqlx::SqlitePool;
async fn updated() -> Result<i32, sqlx::Error> { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/07-update-row.rs"]
mod tests;
