use super::*;
    #[test]
    fn graded() {
        assert_eq!(stack_ops(), (2, 1));
assert_ne!(stack_ops().0, 0);
assert_eq!(stack_ops().1, 1);
    }
