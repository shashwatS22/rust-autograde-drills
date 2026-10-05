use super::*;
    #[test]
    fn graded() {
        assert_eq!(wrap_add(2, 2), Some(4));
assert_eq!(wrap_add(2_000_000, 1), None);
assert!(wrap_add(0, 0).is_some());
    }
