use super::*;
    #[test]
    fn graded() {
        assert_eq!(abs_diff(5, 3), 2);
assert_eq!(abs_diff(3, 5), 2);
assert_eq!(abs_diff(0, 0), 0);
    }
