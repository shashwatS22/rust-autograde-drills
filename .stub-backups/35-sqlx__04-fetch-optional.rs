//! 35-sqlx / 04-fetch-optional
//!
//! TASK
//! Return `Some` when a row exists and `None` when the table is empty.
//!
//! SIGNATURE
//! async fn maybe_one() -> Result<Option<i64>, sqlx::Error>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use sqlx::SqlitePool;
async fn maybe_one() -> Result<Option<i64>, sqlx::Error> { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/04-fetch-optional.rs"]
mod tests;
