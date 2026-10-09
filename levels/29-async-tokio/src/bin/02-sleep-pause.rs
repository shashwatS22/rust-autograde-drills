//! 29-async-tokio / 02-sleep-pause
//!
//! TASK
//! Use tokio::time::pause in test.
//!
//! SIGNATURE
//! async fn delayed() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
async fn delayed() -> i32 { tokio::time::sleep(std::time::Duration::from_secs(60)).await; 1 }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/02-sleep-pause.rs"]
mod tests;