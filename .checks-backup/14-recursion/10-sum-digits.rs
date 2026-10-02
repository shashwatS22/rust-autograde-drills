use super::*;

#[test]
fn digit_sums() {
    assert_eq!(sum_digits(123), 6);
    assert_eq!(sum_digits(0), 0);
}
