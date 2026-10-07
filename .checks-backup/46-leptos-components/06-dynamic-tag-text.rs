use super::*;
    #[test]
    fn graded() {
        assert!(render(7).contains("7"));
assert!(render(0).contains("0"));
assert!(!render(7).is_empty());
    }
