use super::*;
    #[test]
    fn graded() {
        assert!(render().contains("a"));
assert!(render().contains("b"));
assert!(render().matches('p').count() >= 2);
    }
