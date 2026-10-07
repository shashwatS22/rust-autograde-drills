use super::*;
    #[test]
    fn graded() {
        assert_eq!(fields_vs_struct().0, 4);
assert!(fields_vs_struct().0 >= fields_vs_struct().1);
assert_eq!(fields_vs_struct().1, 3);
    }
