use super::*;
    #[test]
    fn graded() {
        assert!(auth(AuthReq { token: "good".into() }).ok);
assert!(!auth(AuthReq { token: "bad".into() }).ok);
assert!(auth(AuthReq { token: "good".into() }).ok);
    }
