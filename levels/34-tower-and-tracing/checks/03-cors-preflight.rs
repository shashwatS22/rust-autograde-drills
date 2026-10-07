use super::*;
use axum::body::Body;
use axum::http::{Request, StatusCode, HeaderValue};
use http_body_util::BodyExt;
use tower::ServiceExt;
#[tokio::test]
async fn graded() {
    let r = app().oneshot(Request::builder().method("OPTIONS").uri("/").header("origin", "http://a.com").header("access-control-request-method", "GET").body(Body::empty()).unwrap()).await.unwrap();
    assert_eq!(r.status(), StatusCode::OK);
    assert!(r.headers().get("access-control-allow-origin").is_some());
}
