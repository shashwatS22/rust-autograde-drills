use super::*;

#[test]
fn adds_two_numbers() {
    assert_eq!(add(2, 3), 5);
    assert_eq!(add(-1, 1), 0);
}

#[test]
fn adds_zero() {
    assert_eq!(add(0, 0), 0);
}
