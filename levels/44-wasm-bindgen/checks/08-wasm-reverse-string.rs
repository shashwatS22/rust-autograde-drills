use super::*;
    #[test]
    fn graded() {
        assert_eq!(rev(), "tsur");
assert_eq!(wasm_reverse(""), "");
assert_eq!(wasm_reverse("a"), "a");
    }
