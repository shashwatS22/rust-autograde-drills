use super::*;
    #[test]
    fn graded() {
        let h = hash_password("secret");
assert!(h.starts_with("$argon2"));
assert!(hash_password("x").contains("argon2"));
    }
