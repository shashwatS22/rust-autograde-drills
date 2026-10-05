use super::*;
    #[test]
    fn graded() {
        assert_eq!(greeting_len(), 11);
assert!(wasm_greet("").starts_with("Hello"));
assert!(wasm_greet("x").contains('x'));
    }
