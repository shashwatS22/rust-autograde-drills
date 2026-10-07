use argon2::{Argon2, PasswordHasher, PasswordVerifier};
use argon2::password_hash::{PasswordHash, SaltString};
fn verify_bad(pwd: &str, hash: &str) -> bool {
    let parsed = PasswordHash::new(hash).unwrap();
    Argon2::default().verify_password(pwd.as_bytes(), &parsed).is_err()
}
fn make_hash(pwd: &str) -> String {
    let salt = SaltString::encode_b64(b"unique16bytesalt").unwrap();
    Argon2::default().hash_password(pwd.as_bytes(), &salt).unwrap().to_string()
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/36-auth-and-config/checks/03-argon2-verify-fail.rs"]
mod tests;
