use super::*;
    #[test]
    fn graded() {
        assert!(bad_args(&["app", "--n", "not-int"]));
assert!(!bad_args(&["app", "--n", "1"]));
assert!(bad_args(&["app", "--n"]));
    }
