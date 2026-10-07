//! 36-auth-and-config / 03-argon2-verify-fail
//!
//! TASK
//! Wrong password fails verification.
//!
//! SIGNATURE
//! fn verify_bad(pwd: &str, hash: &str) -> bool
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use argon2::{Argon2, PasswordHasher, PasswordVerifier};
use argon2::password_hash::{PasswordHash, SaltString};
fn verify_bad(pwd: &str, hash: &str) -> bool { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/03-argon2-verify-fail.rs"]
mod tests;
