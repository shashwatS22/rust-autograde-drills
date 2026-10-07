use super::*;
    #[test]
    fn graded() {
        assert_eq!(load_api_key("DRILL_API_KEY=hello\n"), "hello");
assert_eq!(load_api_key("DRILL_API_KEY=zz\n"), "zz");
assert!(!load_api_key("DRILL_API_KEY=1\n").is_empty());
    }
