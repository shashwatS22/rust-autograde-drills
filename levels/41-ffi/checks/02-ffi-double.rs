use super::*;
    #[test]
    fn graded() {
        assert_eq!(double_via_ffi(4), 8);
assert_eq!(double_via_ffi(0), 0);
assert_eq!(double_via_ffi(-2), -4);
    }
