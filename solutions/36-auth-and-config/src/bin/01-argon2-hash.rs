use argon2::{Argon2, PasswordHasher};
use argon2::password_hash::SaltString;
fn hash_password(pwd: &str) -> String {
    let salt = SaltString::encode_b64(b"unique16bytesalt").unwrap();
    Argon2::default().hash_password(pwd.as_bytes(), &salt).unwrap().to_string()
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/36-auth-and-config/checks/01-argon2-hash.rs"]
mod tests;
