use super::*;

#[test]
fn palindromes() {
    assert!(is_palindrome("racecar"));
    assert!(!is_palindrome("rust"));
}
