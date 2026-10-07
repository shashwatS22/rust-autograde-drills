use super::*;
    #[test]
    fn graded() {
        let h = make_hash("right");
assert!(verify_bad("wrong", &h));
assert!(!verify_bad("right", &h));
    }
