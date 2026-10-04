use super::*;
#[tokio::test]
async fn t() {
    assert_eq!(lock().await, 5)
}
