use super::*;

#[test]
fn even_and_odd() {
    assert!(is_even(4));
    assert!(!is_even(7));
    assert!(is_even(0));
}
