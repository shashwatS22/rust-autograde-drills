//! 35-sqlx / 02-insert-select
//!
//! TASK
//! Insert name into `items` and read it back with a bound parameter.
//!
//! SIGNATURE
//! async fn item_name() -> Result<String, sqlx::Error>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use sqlx::SqlitePool;
async fn item_name() -> Result<String, sqlx::Error> { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/02-insert-select.rs"]
mod tests;
