use super::*;
    #[test]
    fn graded() {
        assert_eq!(bump_unsafe(), 1);
assert_eq!(bump_unsafe(), 2);
assert!(bump_unsafe() >= 3);
    }
