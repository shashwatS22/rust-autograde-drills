use super::*;
        #[tokio::test]
        async fn graded() {
            assert_eq!(updated().await.unwrap(), 10);
assert!(updated().await.unwrap() > 1);
assert!(updated().await.is_ok());
        }
