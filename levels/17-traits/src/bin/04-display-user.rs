//! 17-traits / 04-display-user
//!
//! TASK
//! Implement `Display` for `User`.
//!
//! CONCEPT
//! Display formats values for end users via fmt. write! into the Formatter, like println! but for custom types.
//!
//! SIGNATURE
//! fn format_user() -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::fmt;
struct User { name: String, age: u32 }
impl fmt::Display for User { fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result { todo!() } }
fn format_user() -> String { User { name: "Riya".into(), age: 27 }.to_string() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/04-display-user.rs"]
mod tests;