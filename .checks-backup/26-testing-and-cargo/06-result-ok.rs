use super::*;
    #[test]
    fn graded() {
        assert_eq!(parse_one("7").unwrap(), 7);
assert!(parse_one("x").is_err());
assert!(parse_one("0").is_ok());
    }
