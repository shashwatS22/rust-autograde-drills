use super::*;

#[test]
fn reverses() {
    assert_eq!(reverse(&[1, 2, 3]), vec![3, 2, 1]);
    assert_eq!(reverse(&[]), vec![]);
}
