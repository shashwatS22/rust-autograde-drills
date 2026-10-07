//! 36-auth-and-config / 05-jwt-reject
//!
//! TASK
//! Reject a token signed with a different secret.
//!
//! SIGNATURE
//! fn decode_fails(token: &str, secret: &[u8]) -> bool
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use jsonwebtoken::{decode, DecodingKey, Validation, encode, Header, EncodingKey};
use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct Claims { sub: String, exp: usize }
fn decode_fails(token: &str, secret: &[u8]) -> bool { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/05-jwt-reject.rs"]
mod tests;
