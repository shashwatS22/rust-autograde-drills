use super::*;
    #[test]
    fn graded() {
        assert_eq!(add_via_ffi(2, 3), 5);
assert_eq!(add_via_ffi(0, 0), 0);
assert_eq!(add_via_ffi(-1, 1), 0);
    }
