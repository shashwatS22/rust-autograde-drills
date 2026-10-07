use super::*;
    #[test]
    fn graded() {
        assert!(render().contains("card"));
assert!(render().contains("ok"));
assert!(render().contains("div"));
    }
