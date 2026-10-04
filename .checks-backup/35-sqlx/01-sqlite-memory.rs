use super::*;
#[tokio::test]
async fn t() { assert_eq!(count_users().await.unwrap(), 1); }
