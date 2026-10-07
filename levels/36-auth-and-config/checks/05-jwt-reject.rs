use super::*;
    #[test]
    fn graded() {
        let t = mint(b"ignored");
assert!(decode_fails(&t, b"sekrit"));
assert!(decode_fails(&t, b"nope"));
    }
