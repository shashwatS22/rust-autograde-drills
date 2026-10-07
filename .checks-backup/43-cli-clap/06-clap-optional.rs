use super::*;
    #[test]
    fn graded() {
        assert_eq!(parse_label(&["app", "x"]), Some("x".into()));
assert_eq!(parse_label(&["app"]), None);
assert!(parse_label(&["app", "a"]).is_some());
    }
