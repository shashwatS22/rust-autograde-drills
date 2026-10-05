use super::*;
        #[tokio::test]
        async fn graded() {
            assert_eq!(max_val().await.unwrap(), 7);
assert!(max_val().await.unwrap() > 3);
assert!(max_val().await.is_ok());
        }
