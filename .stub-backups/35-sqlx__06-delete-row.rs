//! 35-sqlx / 06-delete-row
//!
//! TASK
//! Delete a row by id and return remaining count.
//!
//! SIGNATURE
//! async fn after_delete() -> Result<i64, sqlx::Error>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use sqlx::SqlitePool;
async fn after_delete() -> Result<i64, sqlx::Error> { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/06-delete-row.rs"]
mod tests;