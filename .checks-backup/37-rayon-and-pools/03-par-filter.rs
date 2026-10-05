use super::*;
    #[test]
    fn graded() {
        assert_eq!(evens(), vec![2, 4, 6]);
assert!(!evens().contains(&1));
assert_eq!(evens().len(), 3);
    }
