use super::*;
        #[tokio::test]
        async fn graded() {
            assert_eq!(maybe_one().await.unwrap(), Some(9));
assert!(maybe_one().await.unwrap().is_some());
assert!(maybe_one().await.is_ok());
        }
