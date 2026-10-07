use super::*;
    #[test]
    fn graded() {
        assert!(json_key().contains("user_name"));
assert!(!json_key().contains("\"name\""));
assert_eq!(serde_json::from_str::<User>(&json_key()).unwrap().name, "x");
    }
