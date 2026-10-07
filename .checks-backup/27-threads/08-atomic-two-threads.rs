use super::*;
    #[test]
    fn graded() {
        assert_eq!(two_thread_inc(), 2);
assert!(two_thread_inc() >= 2);
assert_ne!(two_thread_inc(), 0);
    }
