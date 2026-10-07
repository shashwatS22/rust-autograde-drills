use super::*;
use axum::body::Body;
use axum::http::{Request, StatusCode, HeaderValue};
use http_body_util::BodyExt;
use tower::ServiceExt;
#[tokio::test]
async fn graded() {
    let r = app().oneshot(Request::builder().uri("/").body(Body::empty()).unwrap()).await.unwrap();
    assert_eq!(r.headers().get("x-drill").unwrap(), "1");
}
