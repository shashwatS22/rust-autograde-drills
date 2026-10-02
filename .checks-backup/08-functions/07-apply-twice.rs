use super::*;

#[test]
fn applies() {
    assert_eq!(apply_twice(|x| x + 1, 5), 7);
    assert_eq!(apply_twice(|x| x * 2, 3), 12);
}
