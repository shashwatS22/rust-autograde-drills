use anyhow::Context;
fn ctx(s: &str) -> anyhow::Result<i32> { s.parse().context("parse") }
fn c() -> anyhow::Result<i32> { ctx("1") }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/25-error-design/checks/04-context.rs"]
mod tests;
