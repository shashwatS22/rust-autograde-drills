use super::*;
    #[test]
    fn graded() {
        assert!(strict_err());
assert!(serde_json::from_str::<User>(r#"{"name":"a"}"#).is_ok());
assert!(strict_err());
    }
