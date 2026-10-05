use super::*;
    #[test]
    fn graded() {
        assert_eq!(doubled(), 8);
assert_eq!(wasm_double(0), 0);
assert_eq!(wasm_double(-3), -6);
    }
