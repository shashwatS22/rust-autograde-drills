use super::*;
    #[test]
    fn graded() {
        assert_eq!(no_double_free(), "keep");
assert_eq!(no_double_free().len(), 4);
assert!(!no_double_free().is_empty());
    }
