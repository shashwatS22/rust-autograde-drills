use super::*;
    #[test]
    fn graded() {
        assert!(render().contains("3"));
assert!(render().contains("em"));
assert!(!render().is_empty());
    }
