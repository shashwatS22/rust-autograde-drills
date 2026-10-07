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
use axum::{extract::Path, routing::get, Router};
async fn pick(Path(code): Path<u16>) -> Result<&'static str, AppError> {
    if code == 404 { Err(AppError::NotFound) } else if code == 400 { Err(AppError::BadRequest) } else { Ok("fine") }
}
pub fn app() -> Router { Router::new().route("/code/{code}", get(pick)) }
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/33-axum-errors/checks/06-branch-error.rs"]
mod tests;
