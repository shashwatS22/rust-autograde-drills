//! 33-axum-errors / 08-map-to-response
//!
//! TASK
//! Map `Result` to response with `match` and `into_response()`.
//!
//! SIGNATURE
//! fn app() -> axum::Router
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
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
    todo!()
}
pub fn app() -> Router { todo!() }
fn main() {}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-map-to-response.rs"]
mod tests;