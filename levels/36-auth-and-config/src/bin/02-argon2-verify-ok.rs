//! 36-auth-and-config / 02-argon2-verify-ok
//!
//! TASK
//! Verify a password against an argon2 hash.
//!
//! SIGNATURE
//! fn verify_ok(pwd: &str, hash: &str) -> bool
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use argon2::{Argon2, PasswordHasher, PasswordVerifier};
use argon2::password_hash::{PasswordHash, SaltString};
fn verify_ok(pwd: &str, hash: &str) -> bool { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/02-argon2-verify-ok.rs"]
mod tests;