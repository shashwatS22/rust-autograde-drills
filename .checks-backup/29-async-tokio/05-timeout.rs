use super::*;
        #[tokio::test]
        async fn graded() {
            tokio::time::pause();
let h = tokio::spawn(timeout_fires());
tokio::time::advance(std::time::Duration::from_secs(1)).await;
assert!(h.await.unwrap());
        }
