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
async fn missing() -> Result<&'static str, AppError> { Err(AppError::NotFound) }
pub fn app() -> Router { Router::new().route("/missing", get(missing)) }
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/33-axum-errors/checks/01-not-found.rs"]
mod tests;
