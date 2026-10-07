use super::*;
    #[test]
    fn graded() {
        assert_eq!(divide(10, 2), 5);
assert!(std::panic::catch_unwind(|| divide(1, 0)).is_err());
assert_eq!(divide(9, 3), 3);
    }
