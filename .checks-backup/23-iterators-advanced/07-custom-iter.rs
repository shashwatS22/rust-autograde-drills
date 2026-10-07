use super::*;
    #[test]
    fn graded() {
        assert_eq!(collect_counter(), vec![0, 1, 2]);
assert_eq!(collect_counter().len(), 3);
assert_eq!(collect_counter()[0], 0);
    }
