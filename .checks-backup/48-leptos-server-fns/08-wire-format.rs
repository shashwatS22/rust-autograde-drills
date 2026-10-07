use super::*;
    #[test]
    fn graded() {
        assert!(wire().contains("true"));
assert!(serde_json::from_str::<OkResp>(&wire()).unwrap().ok);
assert!(!wire().is_empty());
    }
