use super::*;
    #[test]
    fn graded() {
        assert_eq!(ok(), Ok(vec![1, 2]));
assert!(bad().is_err());
assert_eq!(ok().unwrap().len(), 2);
    }
