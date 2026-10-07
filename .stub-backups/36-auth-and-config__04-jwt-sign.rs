//! 36-auth-and-config / 04-jwt-sign
//!
//! TASK
//! Sign a JWT with `jsonwebtoken`.
//!
//! SIGNATURE
//! fn sign_token(sub: &str, secret: &[u8]) -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use jsonwebtoken::{encode, Header, EncodingKey};
use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct Claims { sub: String, exp: usize }
fn sign_token(sub: &str, secret: &[u8]) -> String { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/04-jwt-sign.rs"]
mod tests;
