use super::*;
    #[test]
    fn graded() {
        assert_eq!(init_on_stack(), 42);
assert_ne!(init_on_stack(), 0);
assert!(init_on_stack() > 0);
    }
