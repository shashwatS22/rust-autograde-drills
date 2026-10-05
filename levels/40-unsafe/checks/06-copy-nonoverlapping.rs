use super::*;
    #[test]
    fn graded() {
        assert_eq!(copy_two(), [1, 2]);
assert_ne!(copy_two(), [0, 0]);
assert_eq!(copy_two()[1], 2);
    }
