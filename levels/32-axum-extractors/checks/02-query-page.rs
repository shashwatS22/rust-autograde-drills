use super::*;
use axum::body::Body;
use axum::http::{Request, StatusCode};
use http_body_util::BodyExt;
use tower::ServiceExt;
#[tokio::test]
async fn graded() {
    let r = app().oneshot(Request::builder().uri("/list?page=3").body(Body::empty()).unwrap()).await.unwrap();
    assert_eq!(r.into_body().collect().await.unwrap().to_bytes(), "3");
}
