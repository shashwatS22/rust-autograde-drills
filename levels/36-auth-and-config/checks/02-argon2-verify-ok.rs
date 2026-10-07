use super::*;
    #[test]
    fn graded() {
        let h = make_hash("pw");
assert!(verify_ok("pw", &h));
assert!(verify_ok("pw", &make_hash("pw")));
    }
