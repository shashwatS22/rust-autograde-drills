use super::*;
    #[test]
    fn graded() {
        let t = sign_token("ada", b"sekrit");
assert_eq!(t.split('.').count(), 3);
assert!(!sign_token("x", b"k").is_empty());
    }
