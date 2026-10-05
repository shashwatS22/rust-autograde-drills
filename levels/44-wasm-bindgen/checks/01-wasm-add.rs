use super::*;
    #[test]
    fn graded() {
        assert_eq!(run_add(), 5);
assert_eq!(wasm_add(0, 0), 0);
assert_eq!(wasm_add(-1, 1), 0);
    }
