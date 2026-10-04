use super::*;
#[tokio::test]
async fn t() {
    assert_eq!(both().await, (1, 2))
}
