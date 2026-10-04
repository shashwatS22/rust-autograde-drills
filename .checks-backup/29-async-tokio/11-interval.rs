use super::*;
#[tokio::test]
async fn t() {
    assert_eq!(once().await, 1)
}
