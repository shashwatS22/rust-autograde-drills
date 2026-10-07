use super::*;
use axum::body::Body;
use axum::http::{Request, StatusCode, HeaderValue};
use http_body_util::BodyExt;
use tower::ServiceExt;
#[tokio::test]
async fn graded() {
    let r = app().oneshot(Request::builder().uri("/").header("origin", "http://b.com").body(Body::empty()).unwrap()).await.unwrap();
    assert_eq!(r.headers().get("x-stack").unwrap(), "yes");
}
