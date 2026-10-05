use super::*;
    #[test]
    fn graded() {
        assert_eq!(sum_three(), 6);
assert_eq!(wasm_sum_slice(&[]), 0);
assert_eq!(wasm_sum_slice(&[-1, 1]), 0);
    }
