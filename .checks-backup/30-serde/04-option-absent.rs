use super::*;
    #[test]
    fn graded() {
        assert_eq!(nick(), None);
let with: User = serde_json::from_str(r#"{"name":"a","nick":"z"}"#).unwrap();
assert_eq!(with.nick.as_deref(), Some("z"));
    }
