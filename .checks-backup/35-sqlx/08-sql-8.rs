use super::*;
#[tokio::test]
async fn t() {
    assert_eq!(val().await, 8)
}
