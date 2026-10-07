use super::*;
    #[test]
    fn graded() {
        assert!(round_json().contains("n"));
assert_eq!(serde_json::from_str::<PingReq>(&round_json()).unwrap().n, 1);
assert!(!round_json().is_empty());
    }
