use super::*;
    #[test]
    fn graded() {
        assert!(kind().contains("Ping"));
let pong = serde_json::to_string(&Msg::Pong).unwrap();
assert_eq!(serde_json::from_str::<Msg>(&pong).unwrap(), Msg::Pong);
    }
