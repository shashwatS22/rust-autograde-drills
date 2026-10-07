use super::*;
    #[test]
    fn graded() {
        assert!(render().contains("in"));
assert!(render().contains("div"));
assert!(render().contains("span"));
    }
