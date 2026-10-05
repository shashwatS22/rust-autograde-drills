use super::*;
    #[test]
    fn graded() {
        assert_eq!(sorted(), vec![0, 1, 2, 3, 4]);
assert_eq!(sorted().first(), Some(&0));
assert_eq!(sorted().last(), Some(&4));
    }
