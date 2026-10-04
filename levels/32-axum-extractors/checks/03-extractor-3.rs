use super::*;
use axum::body::Body;
use axum::http::{Request, StatusCode};
use http_body_util::BodyExt;
use tower::ServiceExt;
#[tokio::test]
async fn t() {
    let body = Body::from("{\"n\":3}");
    let response = app().oneshot(Request::builder().method("POST").uri("/").header("content-type", "application/json").body(body).unwrap()).await.unwrap();
    assert_eq!(response.status(), StatusCode::OK);
}
