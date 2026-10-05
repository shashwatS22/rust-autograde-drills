use super::*;
    #[test]
    fn graded() {
        assert_eq!(read_byte(), 5);
assert_ne!(read_byte(), 0);
assert!(read_byte() <= 255);
    }
