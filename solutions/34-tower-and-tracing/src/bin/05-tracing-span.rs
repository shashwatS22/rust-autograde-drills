use axum::{routing::get, Router};
async fn traced() -> &'static str {
    let span = tracing::info_span!("handler", item = "book");
    let _enter = span.enter();
    "traced"
}
pub fn app() -> Router { Router::new().route("/", get(traced)) }
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/34-tower-and-tracing/checks/05-tracing-span.rs"]
mod tests;
