use super::*;
#[tokio::test]
async fn t() {
    assert_eq!(chan().await, 9)
}
