use super::*;
    #[test]
    fn graded() {
        assert_eq!(inc_via_ffi(9), 10);
assert_eq!(inc_via_ffi(-1), 0);
assert_eq!(inc_via_ffi(0), 1);
    }
