use super::*;
    #[test]
    fn graded() {
        assert_eq!(round(), r#"{"name":"a"}"#);
let back: User = serde_json::from_str(&round()).unwrap();
assert_eq!(back.name, "a");
    }
