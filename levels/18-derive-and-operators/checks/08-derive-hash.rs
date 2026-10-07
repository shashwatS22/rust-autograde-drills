use super::*;
    #[test]
    fn graded() {
        assert_eq!(uniq_keys(), 2);
assert!(uniq_keys() >= 1);
assert_ne!(uniq_keys(), 3);
    }
