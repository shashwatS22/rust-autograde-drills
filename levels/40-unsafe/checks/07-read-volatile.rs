use super::*;
    #[test]
    fn graded() {
        assert_eq!(read_volatile(), 99);
assert_ne!(read_volatile(), 0);
assert!(read_volatile() > 50);
    }
