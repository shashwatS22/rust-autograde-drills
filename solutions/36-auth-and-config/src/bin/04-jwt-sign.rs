use jsonwebtoken::{encode, Header, EncodingKey};
use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct Claims { sub: String, exp: usize }
fn sign_token(sub: &str, secret: &[u8]) -> String {
    let claims = Claims { sub: sub.into(), exp: 9_999_999_999 };
    encode(&Header::default(), &claims, &EncodingKey::from_secret(secret)).unwrap()
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/36-auth-and-config/checks/04-jwt-sign.rs"]
mod tests;
