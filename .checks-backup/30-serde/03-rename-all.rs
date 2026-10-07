use super::*;
    #[test]
    fn graded() {
        assert!(camel().contains("firstName"));
assert!(!camel().contains("first_name"));
assert_eq!(serde_json::from_str::<User>(&camel()).unwrap().first_name, "a");
    }
