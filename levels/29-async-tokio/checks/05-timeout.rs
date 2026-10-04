use super::*;
#[tokio::test]
async fn t() {
    assert_eq!(fast().await, 2)
}
