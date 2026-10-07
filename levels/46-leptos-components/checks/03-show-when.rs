use super::*;
    #[test]
    fn graded() {
        assert!(render(true).contains("yes"));
assert!(render(false).contains("no"));
assert!(!render(false).contains("yes"));
    }
