use super::*;
#[tokio::test]
async fn t() {
    assert_eq!(pick().await, 1)
}
