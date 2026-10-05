use super::*;
    #[test]
    fn graded() {
        assert_eq!(parse_ascii(), "rust");
assert_eq!(parse_ascii().len(), 4);
assert!(!parse_ascii().is_empty());
    }
