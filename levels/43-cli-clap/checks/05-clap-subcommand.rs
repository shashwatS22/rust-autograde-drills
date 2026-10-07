use super::*;
    #[test]
    fn graded() {
        assert_eq!(sub_name(&["app", "list"]), "list");
assert_eq!(sub_name(&["app", "add", "1"]), "add");
assert_ne!(sub_name(&["app", "list"]), "add");
    }
