use super::*;
    #[test]
    fn graded() {
        assert_eq!(default_retries(), 3);
assert_eq!(Config::default().timeout_ms, 1000);
assert!(default_retries() > 0);
    }
