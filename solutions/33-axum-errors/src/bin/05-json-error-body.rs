use axum::{http::StatusCode, response::IntoResponse, routing::get, Json, Router};
use serde::Serialize;
#[derive(Serialize)]
struct ErrBody { msg: &'static str }
async fn fail() -> impl IntoResponse { (StatusCode::UNPROCESSABLE_ENTITY, Json(ErrBody { msg: "nope" })) }
pub fn app() -> Router { Router::new().route("/fail", get(fail)) }
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/33-axum-errors/checks/05-json-error-body.rs"]
mod tests;
