//! 36-auth-and-config / 01-argon2-hash
//!
//! TASK
//! Hash a password with `argon2`.
//!
//! CONCEPT
//! argon2 hashes passwords with a salt; never store plain text passwords.
//!
//! SIGNATURE
//! fn hash_password(pwd: &str) -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use argon2::{Argon2, PasswordHasher};
use argon2::password_hash::SaltString;
fn hash_password(pwd: &str) -> String { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-argon2-hash.rs"]
mod tests;