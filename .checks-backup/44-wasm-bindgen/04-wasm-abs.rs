use super::*;
    #[test]
    fn graded() {
        assert_eq!(abs_val(), 7);
assert_eq!(wasm_abs(0), 0);
assert_eq!(wasm_abs(5), 5);
    }
