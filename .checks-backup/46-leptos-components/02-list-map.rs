use super::*;
    #[test]
    fn graded() {
        assert!(render().contains("1"));
assert!(render().contains("2"));
assert!(render().contains("li"));
    }
