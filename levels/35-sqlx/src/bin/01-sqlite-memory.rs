//! 35-sqlx / 01-sqlite-memory
//!
//! TASK
//! Query sqlite memory db.
//!
//! SIGNATURE
//! async fn count_users() -> Result<i64, sqlx::Error>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use sqlx::SqlitePool;
async fn count_users() -> Result<i64, sqlx::Error> { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-sqlite-memory.rs"]
mod tests;
