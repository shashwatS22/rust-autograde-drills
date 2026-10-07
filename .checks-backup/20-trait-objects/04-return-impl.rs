use super::*;
    #[test]
    fn graded() {
        assert_eq!(greet(), "Hi Ada");
assert!(greet().contains("Ada"));
assert!(!greet().is_empty());
    }
