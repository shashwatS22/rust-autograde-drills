use super::*;
        use axum::body::Body;
        use axum::http::{Request, StatusCode};
        use tower::ServiceExt;

        #[tokio::test]
        async fn route_works() {
            let response = app()
    .oneshot(Request::builder().uri("/r8").body(Body::empty()).unwrap())
    .await
    .unwrap();
assert_eq!(response.status(), StatusCode::OK);
        }
