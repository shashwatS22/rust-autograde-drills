use jsonwebtoken::{decode, DecodingKey, Validation, encode, Header, EncodingKey};
use serde::{Deserialize, Serialize};
#[derive(Serialize, Deserialize)]
struct Claims { sub: String, exp: usize }
fn decode_fails(token: &str, secret: &[u8]) -> bool {
    decode::<Claims>(token, &DecodingKey::from_secret(secret), &Validation::default()).is_err()
}
fn mint(secret: &[u8]) -> String {
    encode(&Header::default(), &Claims { sub: "u".into(), exp: 9_999_999_999 }, &EncodingKey::from_secret(b"other")).unwrap()
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/36-auth-and-config/checks/05-jwt-reject.rs"]
mod tests;
