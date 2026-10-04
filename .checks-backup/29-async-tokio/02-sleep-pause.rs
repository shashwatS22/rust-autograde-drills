use super::*;
#[tokio::test]
async fn t() { tokio::time::pause(); let h = tokio::spawn(delayed()); tokio::time::advance(std::time::Duration::from_secs(60)).await; assert_eq!(h.await.unwrap(), 1); }
