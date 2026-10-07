use super::*;
    #[test]
    fn graded() {
        assert_eq!(greet("Ada"), "Hello, Ada!");
assert!(greet("x").starts_with("Hello"));
assert!(greet("").ends_with('!'));
    }
