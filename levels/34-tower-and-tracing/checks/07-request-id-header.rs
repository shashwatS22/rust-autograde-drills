use super::*;
use axum::body::Body;
use axum::http::{Request, StatusCode, HeaderValue};
use http_body_util::BodyExt;
use tower::ServiceExt;
#[tokio::test]
async fn graded() {
    let r = app().oneshot(Request::builder().uri("/").header("x-request-id", "abc-9").body(Body::empty()).unwrap()).await.unwrap();
    assert_eq!(r.into_body().collect().await.unwrap().to_bytes(), "abc-9");
}
