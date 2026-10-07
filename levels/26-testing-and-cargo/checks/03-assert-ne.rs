use super::*;
    #[test]
    fn graded() {
        assert_ne!(not_zero(1), false);
assert_eq!(not_zero(0), false);
assert!(not_zero(5));
    }
