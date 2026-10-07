use axum::http::StatusCode;
use axum::response::{IntoResponse, Response};

#[derive(Debug)]
enum AppError {
    NotFound,
    BadRequest,
}

impl IntoResponse for AppError {
    fn into_response(self) -> Response {
        match self {
            AppError::NotFound => (StatusCode::NOT_FOUND, "not found").into_response(),
            AppError::BadRequest => (StatusCode::BAD_REQUEST, "bad request").into_response(),
        }
    }
}
use axum::{routing::get, Router};
async fn wrapped(flag: bool) -> axum::response::Response {
    let r: Result<&str, AppError> = if flag { Ok("yes") } else { Err(AppError::BadRequest) };
    match r { Ok(v) => v.into_response(), Err(e) => e.into_response() }
}
async fn yes() -> axum::response::Response { wrapped(true).await }
pub fn app() -> Router { Router::new().route("/yes", get(yes)) }
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/33-axum-errors/checks/08-map-to-response.rs"]
mod tests;
