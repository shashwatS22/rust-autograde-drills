use super::*;
    #[test]
    fn graded() {
        assert_eq!(echo(EchoReq { msg: None }).msg, "none");
assert_eq!(echo(EchoReq { msg: Some("x".into()) }).msg, "x");
assert_eq!(echo(EchoReq { msg: None }).msg, "none");
    }
