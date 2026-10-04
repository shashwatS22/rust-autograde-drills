use super::*;
#[tokio::test]
async fn t() {
    assert_eq!(spawned().await, 4)
}
