use super::*;

#[test]
fn finds_min_max() {
    assert_eq!(min_max(&[3, 1, 4]), (1, 4));
    assert_eq!(min_max(&[-5, -2, -9]), (-9, -2));
}
